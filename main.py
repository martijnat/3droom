#!/usr/bin/env python3

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import sys
import pygame
import time
import math
import random
from math import sin, cos, pi, atan,sqrt
from engine import *

# Set to true or when you can't achieve 50 frames per second
DEBUG = True
LOWPOWER = False
key_press = keypress()
current_sector = None
topdown_max_depth = 5
draw3d_max_depth = 32
topdown_scale = 10
# player_max_move_speed = 0.2
player_accel_rate = 0.08 if LOWPOWER else 0.02
player_move_friction = 0.85 if LOWPOWER else 0.9
player_ddx = 0
player_ddy = 0
move_speed = 0.1
turn_speed = 0.10 if LOWPOWER else 0.05
player_x = -6
player_y = -1
player_z = 0
player_angle = -0.6
height_offset = 9999
player_height = 480
player_jumpdz = -105 if LOWPOWER else -35
player_gravdz = 8 if LOWPOWER else 1
player_dz = 0
max_stair_size = 200
draw_topdown = False
LIVE_LOADING = True
UI_HEIGHT = 32
min_clip_dist = 0.1


allcolors = [ gb_black , gb_black2 , gb_red , gb_red2 , gb_green ,
              gb_green2 , gb_yellow , gb_yellow2 , gb_blue , gb_blue2 , gb_magenta ,
              gb_magenta2 , gb_cyan , gb_cyan2 , gb_white , gb_white2 , ]


secret_unlocked = [False]*4


def drawUI(current_sector):
    pygame.draw.rect(screen, gb_black, (0, height - UI_HEIGHT, width, height), 0)
    draw_text(height-UI_HEIGHT,0," "+current_sector.str_name,gb_white2)
    # mouse_deadzone
    # draw_line(-mouse_deadzone,-mouse_deadzone,-mouse_deadzone,mouse_deadzone,gb_black2)
    # draw_line(-mouse_deadzone,-mouse_deadzone,mouse_deadzone,-mouse_deadzone,gb_white2)
    # draw_line(-mouse_deadzone,mouse_deadzone,mouse_deadzone,mouse_deadzone,gb_white2)
    # draw_line(mouse_deadzone,-mouse_deadzone,mouse_deadzone,mouse_deadzone,gb_black2)



def intersect(x1, y1, x2, y2, h):
    if y1 < y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    vis_dist = y1 - h
    invis_dist = h - y2
    vis_ratio = vis_dist / float(vis_dist + invis_dist)
    new_x = x1 + vis_ratio * (x2 - x1)
    new_y = y1 + vis_ratio * (y2 - y1)
    return new_x, new_y


class vector():

    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        return vector([l + r for l, r in zip(self.elements, other.elements)])

    def __mul__(self, scalar):
        return vector([e * scalar for e in self.elements])

    def dot(self, other):
        return sum([l * r for l, r in zip(self.elements, other.elements)])

    def split(self):
        return self.elements

    def normalize(self):
        size = sqrt(self.dot(self))
        if size > 0:
            return vector([self.elements[0] / float(size), self.elements[1] / float(size)])
        return vector([0,0])


class wall():
    scale = 480
    min_dist = 0.01

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.portal = False
        self.next_sector = None

    def draw(self, x, y, a, color_ceil, color_wall, color_floor, min_x, max_x, lty, lby, rty, rby,height,elevation,absolute_elevation,topdown,depth = 0):
        if depth > draw3d_max_depth:
            return
        if max_x < min_x:
            return

        # Caluclate 2d coordinates
        rx1 = cos(a) * (self.x1 - x) - sin(a) * (self.y1 - y)
        ry1 = -cos(a) * (self.y1 - y) - sin(a) * (self.x1 - x)
        rx2 = cos(a) * (self.x2 - x) - sin(a) * (self.y2 - y)
        ry2 = -cos(a) * (self.y2 - y) - sin(a) * (self.x2 - x)

        # If both edges of the wall are behind the player, we dont need to draw anything
        if ry1 <= wall.min_dist and ry2 <= wall.min_dist:
            return

        # If one of the edges of the wall is behind the player, use the intersection with the wall and the screen edge instead
        if ry1 <= wall.min_dist:
            rx1, ry1 = intersect(rx1, ry1, rx2, ry2, wall.min_dist)
        elif ry2 <= wall.min_dist:
            rx2, ry2 = intersect(rx1, ry1, rx2, ry2, wall.min_dist)

        # Now translate the 2d coordinates into a projections
        left_x = rx1 * wall.scale / float(ry1)
        right_x = rx2 * wall.scale / float(ry2)
        bot_ly = (-elevation) / float(ry1)
        top_ly = (-elevation - height) / float(ry1)
        bot_ry = (-elevation) / float(ry2)
        top_ry = (-elevation - height) / float(ry2)

        if abs(right_x - left_x) < wall.min_dist:
            return              # Don't draw the backside of walls

        if right_x <= min_x:
            return
        if left_x >= max_x:
            return


        if self.portal:
            portal_top_ratio = max(0,min(1,(self.next_sector.elevation + self.next_sector.height - absolute_elevation) / float(height)))
            portal_bottom_ratio = max(0,min(1,(self.next_sector.elevation - absolute_elevation) / float(height)))
            self.next_sector.draw(x,
                                  y,
                                  a,
                                  left_x,
                                  right_x,
                                  bot_ly+(top_ly-bot_ly)*portal_top_ratio,
                                  bot_ly+(top_ly-bot_ly)*portal_bottom_ratio,
                                  bot_ry+(top_ry-bot_ry)*portal_top_ratio,
                                  bot_ry+(top_ry-bot_ry)*portal_bottom_ratio,
                                  elevation + self.next_sector.elevation - absolute_elevation,
                                  topdown,
                                  depth+1)
            # Bottom portal edge
            # draw_polygon([
            draw_polygon([
                (left_x,top_ly),
                (right_x,top_ry),
                (right_x,bot_ry + (top_ry-bot_ry)*portal_top_ratio),
                (left_x,bot_ly + (top_ly-bot_ly)*portal_top_ratio),
                ],color_wall,topdown)

            # bottom portal edge
            draw_polygon([
                (left_x,bot_ly + (top_ly-bot_ly)*portal_bottom_ratio),
                (right_x,bot_ry + (top_ry-bot_ry)*portal_bottom_ratio),
                (right_x,bot_ry),
                (left_x,bot_ly),
                ],color_wall,topdown)
        else:
            # Draw Bounding box of the wall
            draw_polygon([(left_x,top_ly), (right_x,top_ry), (right_x,bot_ry), (left_x,bot_ly),],color_wall,topdown)
            pass

        # Draw Bounding box of the ceiling
        draw_polygon([
            (left_x,min(lty,top_ly)),
            (right_x,min(rty,top_ry)),
            (right_x,top_ry),
            (left_x,top_ly),
        ],color_ceil,topdown)

        # Draw Bounding box of the floor
        draw_polygon([
            (left_x,bot_ly),
            (right_x,bot_ry),
            (right_x,max(bot_ry,rby)),
            (left_x,max(bot_ly,lby)),
        ],color_floor,topdown)

    def draw_legacy(self, x, y, a, color_ceil, color_wall, color_floor, min_x, max_x, lty, lby, rty, rby,height,elevation,absolute_elevation,depth = 0):
        min_x = min(height,min_x)
        max_x = max(-height,max_x)
        rx1 = cos(a) * (self.x1 - x) - sin(a) * (self.y1 - y)
        ry1 = -cos(a) * (self.y1 - y) - sin(a) * (self.x1 - x)
        rx2 = cos(a) * (self.x2 - x) - sin(a) * (self.y2 - y)
        ry2 = -cos(a) * (self.y2 - y) - sin(a) * (self.x2 - x)
        player_x = x
        player_y = y

        if ry1 <= wall.min_dist and ry2 <= wall.min_dist:
            return

        if ry1 <= wall.min_dist:
            rx1, ry1 = intersect(rx1, ry1, rx2, ry2, wall.min_dist)
        elif ry2 <= wall.min_dist:
            rx2, ry2 = intersect(rx1, ry1, rx2, ry2, wall.min_dist)

        if max(ry1,ry2) > draw3d_max_depth:
            return

        left_x = rx1 * wall.scale / float(ry1)
        right_x = rx2 * wall.scale / float(ry2)
        if abs(right_x - left_x) < wall.min_dist:
            return

        top_ly = (-elevation) / float(ry1)
        bot_ly = (-elevation - height) / float(ry1)
        top_ry = (-elevation) / float(ry2)
        bot_ry = (-elevation - height) / float(ry2)

        if max_x<=min_x:
            return
        top_portal_angle = (lty-rty)/ float(min_x - max_x)
        bottom_portal_angle = (lby-rby)/ float(min_x - max_x)
        top_wall_angle = (top_ry - top_ly) / float(right_x - left_x)
        bottom_wall_angle = (bot_ry - bot_ly) / float(right_x - left_x)
        y_top = max(top_ly,lty)
        y_bottom = min(bot_ly,lby)
        x_start = left_x

        y_min = min(top_ly,lty)
        y_max = max(bot_ly,lby)
        y_top_angle =  (rty - lty) / float(min_x - max_x)
        y_bottom_angle =  (rty - lty) / float(min_x - max_x)
        if min_x > left_x:
            y_top += top_wall_angle * (min_x - left_x)
            y_bottom += bottom_wall_angle * (min_x - left_x)
            y_min += y_top_angle  * (min_x - left_x)
            y_max += y_bottom_angle  * (min_x - left_x)
            x_start = min_x
        x_end = int(min(max_x, right_x))


        if self.portal:
            if x_start < x_end:
                portal_top_ratio = (self.next_sector.elevation + self.next_sector.height - height - absolute_elevation) / float(height)
                portal_bottom_ratio = (self.next_sector.elevation - absolute_elevation) / float(height)
                y_top_new = portal_top_ratio*(x_end-x_start)
                y_bottom_new = portal_bottom_ratio*(x_end-x_start)

                # draw_line(x_start,y_bottom,x_end,y_bottom +bottom_wall_angle * (x_end-x_start),(255,0,255))
                # draw_line(x_start,y_top,x_end,y_top +top_wall_angle * (x_end-x_start),(255,255,0))

        if x_start >= x_end:
            return
        for x in range(int(x_start), int(x_end), 1):
            draw_column(x, y_min, y_bottom,color_ceil)
            draw_column(x, y_top, y_max,color_floor)
            if not self.portal:
                draw_column(x, y_top, y_bottom,color_wall)
            else:
                self.next_sector.draw(player_x,
                                      player_y,
                                      a,
                                      x,
                                      x+1,
                                      y_min + (portal_top_ratio) * (y_bottom-y_top),
                                      y_max + (portal_bottom_ratio) * (y_bottom-y_top) ,
                                      y_min + (portal_top_ratio) * (y_bottom-y_top),
                                      y_max + (portal_bottom_ratio) * (y_bottom-y_top) ,
                                      elevation + self.next_sector.elevation - absolute_elevation,depth+1)
                if portal_top_ratio < 0:
                    draw_column(x, y_bottom + (portal_top_ratio) * (y_bottom-y_top) , y_bottom,color_wall)
                if portal_bottom_ratio > 0:
                    draw_column(x, y_top + (portal_bottom_ratio) * (y_bottom-y_top) , y_top,color_wall)
                pass
            y_top += top_wall_angle
            y_bottom += bottom_wall_angle
            y_max += bottom_portal_angle
            y_min += top_portal_angle

    def draw_topdown(self, x, y, a, depth):
        # calculate points relative to player position
        rx1 = cos(a) * (self.x1 - x) - sin(a) * (self.y1 - y)
        ry1 = cos(a) * (self.y1 - y) + sin(a) * (self.x1 - x)
        rx2 = cos(a) * (self.x2 - x) - sin(a) * (self.y2 - y)
        ry2 = cos(a) * (self.y2 - y) + sin(a) * (self.x2 - x)

        rx1,ry1,rx2,ry2 = [_ * topdown_scale for _ in [rx1,ry1,rx2,ry2]]

        if depth == 0:
            draw_line(rx1, ry1, rx2, ry2, gb_cyan2)
        else:
            draw_line(rx1, ry1, rx2, ry2, gb_white2)

    def position_relative(self, x, y):
        position = (self.x2 - self.x1) * (y - self.y1) - \
            (self.y2 - self.y1) * (x - self.x1)
        return position

    def closest_point_on_wall(self, x, y):
        A = vector([self.x1, self.y1])
        AP = vector([x - self.x1, y - self.y1])
        AB = vector([self.x2 - self.x1, self.y2 - self.y1])

        point_on_wall = A + (AB * (AP.dot(AB) / float(AB.dot(AB))))

        direction_from_wall = (vector([-x,-y]) + point_on_wall).normalize()

        return point_on_wall + direction_from_wall * min_clip_dist


def join_sectorlist(all_sectors):
    for i in range(len(all_sectors)):
        for j in range(i+1,len(all_sectors)):
            join_sectors(all_sectors[i],all_sectors[j])

def join_sectors(s1, s2):
    portals_made = False
    for w1 in s1.walls:
        for w2 in s2.walls:
            if w1.x1 == w2.x2 and\
               w1.x2 == w2.x1 and\
               w1.y1 == w2.y2 and\
               w1.y2 == w2.y1:
                w1.portal = True
                w2.portal = True
                w1.next_sector = s2
                w2.next_sector = s1
                portals_made = True
    if portals_made:
        s2.joined_sectors.append(s1)
        s1.joined_sectors.append(s2)

def join_oneway(s1, s2):
    portals_made = False
    for w1 in s1.walls:
        for w2 in s2.walls:
            if w1.x1 == w2.x2 and\
               w1.x2 == w2.x1 and\
               w1.y1 == w2.y2 and\
               w1.y2 == w2.y1:
                w1.portal = True
                w1.next_sector = s2
                portals_made = True
    if portals_made:
        s1.joined_sectors.append(s2)



class sector():
    facecounter = 0
    def __init__(self, wallcoords, color_ceil, color_wall, color_floor,elevation = 0,top = 1600,str_name = ""):
        wallcount = len(wallcoords)
        self.walls = [wall(wallcoords[i],wallcoords[i+1],wallcoords[(i+2)%wallcount],wallcoords[(i+3)%wallcount]) for i in range(0,wallcount,2)]
        self.color_ceil = color_ceil
        self.color_wall = color_wall
        self.color_floor = color_floor
        sector.facecounter+=2
        self.joined_sectors = []
        self.elevation = elevation + height_offset
        self.height = top - elevation
        self.rendering = False
        self.td_rendering = False
        self.no_access = False
        self.str_name = str_name

    def draw(self, x, y, a, min_x, max_x, lty, lby, rty, rby,relative_elevation,topdown,depth=0):
        if self.rendering:
            return
        self.rendering = True
        for wall in self.walls:
            wall.draw(x, y, a, self.color_ceil, self.color_wall,
                      self.color_floor, min_x, max_x, lty, lby, rty, rby,self.height,relative_elevation,self.elevation,topdown,depth)
            # pygame.display.flip()
            # time.sleep(0.001)
        self.rendering = False

    def draw_topdown(self, x, y, a, depth=0):
        if self.td_rendering:
            return
        self.td_rendering = True
        if depth < topdown_max_depth:
            for other in self.joined_sectors:
                if not other.td_rendering:
                    other.draw_topdown(x, y, a, depth + 1)
        for wall in self.walls:
            wall.draw_topdown(x, y, a,depth)
        self.td_rendering = False

    def move_to(self, x, y, z):
        if z > -self.elevation:
            z = -self.elevation
        for wall in self.walls:
            if wall.position_relative(x, y) < 0:
                if wall.portal:
                    if wall.next_sector.elevation <= (-z + max_stair_size) and not wall.next_sector.no_access:
                        return wall.next_sector.move_to(x,y,z - self.elevation + wall.next_sector.elevation)
                    else:
                        x, y = wall.closest_point_on_wall(x, y).elements
                else:
                    x, y = wall.closest_point_on_wall(x, y).elements
        return self, x, y, z


last_data = open("data.py").read()
exec(last_data)
current_sector = init_sector
while engine_step(keypress,30 if LOWPOWER else 60):
    if LIVE_LOADING:
        try:
            new_data = open("data.py").read()
            if new_data != last_data:
                last_data = new_data
                exec(new_data)
        except Exception as e:
            print(e)
    new_z = player_z

    if player_z > current_sector.elevation:
        player_dz = 0
        new_z = current_sector.elevation
    else:
        player_dz += player_gravdz

    if keypress.w or keypress.up:
        player_ddx -= player_accel_rate * sin(player_angle)
        player_ddy -= player_accel_rate * cos(player_angle)
    if keypress.s or keypress.down:
        player_ddx += player_accel_rate * sin(player_angle)
        player_ddy += player_accel_rate * cos(player_angle)
    if keypress.a:
        player_ddx += player_accel_rate * sin(player_angle - pi / 2.0)
        player_ddy += player_accel_rate * cos(player_angle - pi / 2.0)
    if keypress.d:
        player_ddx += player_accel_rate * sin(player_angle + pi / 2.0)
        player_ddy += player_accel_rate * cos(player_angle + pi / 2.0)
    if keypress.left:
        player_angle += turn_speed
    if keypress.right:
        player_angle -= turn_speed
    draw_topdown = keypress.tab
    if keypress.space:
        if new_z == -current_sector.elevation:
            player_dz = player_jumpdz

    new_z += player_dz
    player_ddx = player_ddx * player_move_friction
    player_ddy = player_ddy * player_move_friction
    new_x, new_y = player_x + player_ddx, player_y + player_ddy
    current_sector, player_x, player_y,player_z = current_sector.move_to(new_x, new_y,new_z)
    # current_sector.draw(player_x, player_y, player_angle, -width//2, width//2, -height//2, height//2 - UI_HEIGHT, -height//2, height//2 - UI_HEIGHT, player_z - player_height + height_offset,draw_topdown)
    current_sector.draw(player_x, player_y, player_angle, -width//8, width//8, -height//8, height//8, -height//8, height//8, player_z - player_height + height_offset,draw_topdown)
    if draw_topdown:
        current_sector.draw_topdown(player_x, player_y, player_angle)
        draw_line(0,0,0,-height/float(32),gb_red)
        draw_line(0,0,-height/float(64),0,gb_red)
        draw_line(0,0,height/float(64),0,gb_red)
    drawUI(current_sector)

pygame.quit()
