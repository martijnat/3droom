#!/usr/bin/env python3

import sys
import pygame
import time
import math
from math import sin, cos, pi, atan,sqrt
from engine import *

key_press = keypress()
current_sector = None
topdown_max_depth = 8
topdown_scale = 10
move_speed = 0.1
turn_speed = 0.05
player_x = 0
player_y = 0
player_z = 0
height_offset = 9999
player_height = 480
player_jumpdz = -35
player_gravdz = 1
player_dz = 0
player_angle = 0
max_stair_size = 200
draw_topdown = False
LIVE_LOADING = True
UI_HEIGHT = 32
min_clip_dist = 0.1

# shift sprint!
gb_black = pygame.Color(0x1d,  0x20,  0x21,  255)  # 1d2021
gb_black2 = pygame.Color(0x7c,  0x6f,  0x64,  255)  # 7c6f64
gb_red = pygame.Color(0xcc,  0x24,  0x1d,  255)  # cc241d
gb_red2 = pygame.Color(0xfb,  0x49,  0x34,  255)  # fb4934
gb_green = pygame.Color(0x98,  0x97,  0x1a,  255)  # 98971a
gb_green2 = pygame.Color(0xb8,  0xbb,  0x26,  255)  # b8bb26
gb_yellow = pygame.Color(0xd7,  0x99,  0x21,  255)  # d79921
gb_yellow2 = pygame.Color(0xfa,  0xbd,  0x2f,  255)  # fabd2f
gb_blue = pygame.Color(0x45,  0x85,  0x88,  255)  # 458588
gb_blue2 = pygame.Color(0x83,  0xa5,  0x98,  255)  # 83a598
gb_magenta = pygame.Color(0xb1,  0x62,  0x86,  255)  # b16286
gb_magenta2 = pygame.Color(0xd3,  0x86,  0x9b,  255)  # d3869b
gb_cyan = pygame.Color(0x68,  0x9d,  0x6a,  255)  # 689d6a
gb_cyan2 = pygame.Color(0x8e,  0xc0,  0x7c,  255)  # 8ec07c
gb_white = pygame.Color(0xd5, 0xc4, 0xa1)
gb_white2 = pygame.Color(0xf9, 0xf5, 0xd7)


secret_unlocked = [False]*4


def drawUI(current_sector):
    pygame.draw.rect(screen, gb_black, (0, height - UI_HEIGHT, width, height), 0)
    draw_text(height-UI_HEIGHT,0," "+current_sector.str_name,gb_white2)


def intersect(x1, y1, x2, y2, h):
    if y1 < y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    vis_dist = y1 - h
    invis_dist = h - y2
    vis_ratio = vis_dist / (vis_dist + invis_dist)
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
            return vector([self.elements[0] / size, self.elements[1] / size])
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

    def draw(self, x, y, a, color_ceil, color_wall, color_floor, min_x, max_x, lty, lby, rty, rby,height,elevation,absolute_elevation):
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

        left_x = rx1 * wall.scale / ry1
        right_x = rx2 * wall.scale / ry2
        if abs(right_x - left_x) < wall.min_dist:
            return

        top_ly = (-elevation) / ry1
        bot_ly = (-elevation - height) / ry1
        top_ry = (-elevation) / ry2
        bot_ry = (-elevation - height) / ry2


        top_wall_angle = (top_ry - top_ly) / (right_x - left_x)
        bottom_wall_angle = (bot_ry - bot_ly) / (right_x - left_x)
        y_top = top_ly
        y_bottom = bot_ly
        x_start = left_x

        y_min = lty
        y_max = lby
        y_top_angle =  (rty - lty) / (min_x - max_x)
        y_bottom_angle =  (rty - lty) / (min_x - max_x)
        if min_x > left_x:
            y_top += top_wall_angle * (min_x - left_x)
            y_bottom += bottom_wall_angle * (min_x - left_x)
            y_min += y_top_angle  * (min_x - left_x)
            y_max += y_bottom_angle  * (min_x - left_x)
            x_start = min_x
        x_end = int(min(max_x, right_x))


        if self.portal:
            if x_start < x_end:
                self.next_sector.draw(player_x,
                                      player_y,
                                      a,
                                      x_start,
                                      x_end,
                                      y_min,
                                      y_max,
                                      y_min,
                                      y_max,
                                      elevation + self.next_sector.elevation - absolute_elevation)
                portal_top_ratio = (self.next_sector.elevation + self.next_sector.height - height - absolute_elevation) / (height)
                portal_bottom_ratio = (self.next_sector.elevation - absolute_elevation) / (height)

        for x in range(int(x_start), int(x_end), 1):
            draw_column(x, y_min, y_bottom,color_ceil)
            draw_column(x, y_top, y_max,color_floor)
            if not self.portal:
                draw_column(x, y_top, y_bottom,color_wall)
            else:
                if portal_top_ratio < 0:
                    draw_column(x, y_bottom + (portal_top_ratio) * (y_bottom-y_top) , y_bottom,color_wall)
                if portal_bottom_ratio > 0:
                    draw_column(x, y_top + (portal_bottom_ratio) * (y_bottom-y_top) , y_top,color_wall)
                pass
            y_top += top_wall_angle
            y_bottom += bottom_wall_angle
            y_max += y_top_angle
            y_min += y_bottom_angle

    def draw_topdown(self, x, y, a, depth):
        # calculate points relative to player position
        rx1 = cos(a) * (self.x1 - x) - sin(a) * (self.y1 - y)
        ry1 = cos(a) * (self.y1 - y) + sin(a) * (self.x1 - x)
        rx2 = cos(a) * (self.x2 - x) - sin(a) * (self.y2 - y)
        ry2 = cos(a) * (self.y2 - y) + sin(a) * (self.x2 - x)

        rx1,ry1,rx2,ry2 = [_ * topdown_scale for _ in [rx1,ry1,rx2,ry2]]

        if depth == 0:
            draw_line(rx1, ry1, rx2, ry2, green)
        else:
            draw_line(rx1, ry1, rx2, ry2, white)

    def position_relative(self, x, y):
        position = (self.x2 - self.x1) * (y - self.y1) - \
            (self.y2 - self.y1) * (x - self.x1)
        return position

    def closest_point_on_wall(self, x, y):
        A = vector([self.x1, self.y1])
        AP = vector([x - self.x1, y - self.y1])
        AB = vector([self.x2 - self.x1, self.y2 - self.y1])

        point_on_wall = A + (AB * (AP.dot(AB) / AB.dot(AB)))

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


class sector():

    def __init__(self, wallcoords, color_ceil, color_wall, color_floor,elevation = 0,top = 1600,str_name = ""):
        wallcount = len(wallcoords)
        self.walls = [wall(wallcoords[i],wallcoords[i+1],wallcoords[(i+2)%wallcount],wallcoords[(i+3)%wallcount]) for i in range(0,wallcount,2)]
        self.color_ceil = color_ceil
        self.color_wall = color_wall
        self.color_floor = color_floor
        self.joined_sectors = []
        self.elevation = elevation + height_offset
        self.height = top - elevation
        self.rendering = False
        self.str_name = str_name

    def draw(self, x, y, a, min_x, max_x, lty, lby, rty, rby,relative_elevation):
        if self.rendering:
            return
        self.rendering = True
        for wall in self.walls:
            wall.draw(x, y, a, self.color_ceil, self.color_wall,
                      self.color_floor, min_x, max_x, lty, lby, rty, rby,self.height,relative_elevation,self.elevation)
            # pygame.display.flip()
            # time.sleep(0.001)
        self.rendering = False

    def draw_topdown(self, x, y, a, depth=0):
        if self.rendering:
            return
        self.rendering = True
        if depth < topdown_max_depth:
            for other in self.joined_sectors:
                other.draw_topdown(x, y, a, depth + 1)
        for wall in self.walls:
            wall.draw_topdown(x, y, a,depth)
        self.rendering = False

    def move_to(self, x, y, z):
        if z > -self.elevation:
            z = -self.elevation
        for wall in self.walls:
            if wall.position_relative(x, y) < 0:
                if wall.portal:
                    if wall.next_sector.elevation <= (-z + max_stair_size):
                        return wall.next_sector.move_to(x,y,z - self.elevation + wall.next_sector.elevation)
                    else:
                        x, y = wall.closest_point_on_wall(x, y).elements
                else:
                    x, y = wall.closest_point_on_wall(x, y).elements
        return self, x, y, z


last_data = open("data.py").read()
exec(last_data)
current_sector = init_sector
while engine_step(keypress):
    if LIVE_LOADING:
        try:
            new_data = open("data.py").read()
            if new_data != last_data:
                last_data = new_data
                exec(new_data)
        except Exception as e:
            print(e)

    new_x, new_y, new_z = player_x, player_y, player_z
    if player_z > current_sector.elevation:
        player_dz = 0
        new_z = current_sector.elevation
    else:
        player_dz += player_gravdz

    if keypress.w or keypress.up:
        new_x -= move_speed * sin(player_angle)
        new_y -= move_speed * cos(player_angle)
    if keypress.s or keypress.down:
        new_x += move_speed * sin(player_angle)
        new_y += move_speed * cos(player_angle)
    if keypress.a:
        new_x += move_speed * sin(player_angle - pi / 2)
        new_y += move_speed * cos(player_angle - pi / 2)
    if keypress.d:
        new_x += move_speed * sin(player_angle + pi / 2)
        new_y += move_speed * cos(player_angle + pi / 2)
    if keypress.left:
        player_angle += turn_speed
    if keypress.right:
        player_angle -= turn_speed
    if keypress.p:
        draw_topdown = not draw_topdown
        print(player_x,player_y,player_z)
    if keypress.space:
        if new_z == -current_sector.elevation:
            player_dz = player_jumpdz

    new_z += player_dz
    current_sector, player_x, player_y,player_z = current_sector.move_to(new_x, new_y,new_z)
    current_sector.draw(player_x, player_y, player_angle, -width//2, width//2, -height//2, height//2 - UI_HEIGHT, -height//2, height//2, player_z - player_height + height_offset)
    if draw_topdown:
        current_sector.draw_topdown(player_x, player_y, player_angle)
    drawUI(current_sector)

