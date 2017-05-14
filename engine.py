#!/usr/bin/env python3

import sys
import pygame
import pygame.gfxdraw
import random
# import pygame.Color
import time
pygame.init()
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
mainfont = pygame.font.Font("./FSEX300-L.ttf",24)


engine_version = "1.0"
speed = [2, 2]
black = 0, 0, 0

class keypress():
    left   =  False
    right  =  False
    down   =  False
    up     =  False
    w      =  False
    a      =  False
    s      =  False
    d      =  False
    space  =  False


# size = width, height = 320, 240
size = width, height = 640, 480
# size = width, height = 1024, 768
# size = width, height = 1920, 1080
# screen = pygame.display.set_mode(size,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
# screen = pygame.display.set_mode(size,pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
screen = pygame.display.set_mode(size,pygame.DOUBLEBUF | pygame.HWSURFACE)
screen.set_alpha(None)             # Engine is so simple, it does not use an alhpa channel
pygame.mouse.set_visible(False) # invisible mouse
# screen = pygame.display.set_mode(size)

pygame.display.set_caption("Doomlike engine %s"%engine_version)

white = pygame.Color(255, 255, 255, 255)
grey = pygame.Color(128, 128, 128, 255)
red = pygame.Color(255, 0, 0, 255)
green = pygame.Color(0, 255, 0, 255)
blue = pygame.Color(0, 0, 255, 255)

def rgbcolor(r,g,b):
    r,g,b = map((lambda x:int(max(0,min(255,255*x)))),[r,g,b])
    return pygame.Color(r,g,b, 255)

def color(c):
    r,g,b = map((lambda x:int(max(0,min(255,255*x)))),c)
    return pygame.Color(r,g,b, 255)

def depthcolor(c,depth):
    r,g,b = map(lambda x:int(max(0,min(255,(255*x)/depth))),c)
    return pygame.Color(r,g,b, 255)

def randomcolor():
    r = int(128 + 127*random.randrange(2))
    g = int(128 + 127*random.randrange(2))
    b = int(128 + 127*random.randrange(2))
    return pygame.Color(r,g,b, 255)

def random_pixel(x,y):
    draw_pixel(x,y,randomcolor())

def random_line(x1,y1,x2,y2):
    try:
        draw_line(x1,y1,x2,y2,randomcolor())
    except Exception as e:
        print(e)

def draw_pixel(x,y,color=white):
    pygame.gfxdraw.pixel(screen, int(width/2+x), int(height/2+y), color)

def draw_line(x1,y1,x2,y2,color=white):
    try:
        pygame.gfxdraw.line(screen, int(width/2+x1), int(height/2+y1), int(width/2+x2), int(height/2+y2), color)
    except Exception as e:
        print(e)

def draw_text(h,w,msg,color):
    # render text
    label = mainfont.render(msg, 1, color)
    screen.blit(label, (w, h))

def draw_column(x,y_top,y_bottom,color):
    # color = fog_color(color,wall_angle)
    try:
        pygame.gfxdraw.line(screen, int(width/2+x), int(height/2+y_top), int(width/2+x), int(height/2+y_bottom), color)
    except:
        pass
        # pygame.gfxdraw.pixel(screen, int(width/2+x), int(height/2+y_top), black)
    # pygame.gfxdraw.pixel(screen, int(width/2+x), int(height/2+y_bottom), black)
    # pygame.display.flip()
    # time.sleep(0.001)

def draw_triangle(x1,y1,x2,y2,x3,y3,color=white):
    pygame.draw.polygon(screen, color,
                        [[int(width/2+x1), int(height/2+y1)],
                         [int(width/2+x2), int(height/2+y2)],
                         [int(width/2+x3), int(height/2+y3)]])


clock = pygame.time.Clock()

def engine_step(keypress=keypress(),framerate=60):
    global screen,height,width
    clock.tick(framerate)
    pygame.display.flip()
    # screen.fill(black)
    keypress.p = False          # debug key

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.VIDEORESIZE:
            width,height=event.size
            screen = pygame.display.set_mode(event.size)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keypress.left = True
            elif event.key == pygame.K_RIGHT:
                keypress.right = True
            elif event.key == pygame.K_UP:
                keypress.up = True
            elif event.key == pygame.K_DOWN:
                keypress.down = True
            elif event.key == pygame.K_SPACE:
                keypress.space = True
            elif event.key == pygame.K_w:
                keypress.w = True
            elif event.key == pygame.K_a:
                keypress.a = True
            elif event.key == pygame.K_s:
                keypress.s = True
            elif event.key == pygame.K_d:
                keypress.d = True
            elif event.key == pygame.K_p:
                keypress.p = True
            elif event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            elif event.key == pygame.K_ESCAPE:
                return False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keypress.left = False
            elif event.key == pygame.K_RIGHT:
                keypress.right = False
            elif event.key == pygame.K_UP:
                keypress.up = False
            elif event.key == pygame.K_DOWN:
                keypress.down = False
            elif event.key == pygame.K_SPACE:
                keypress.space = False
            elif event.key == pygame.K_w:
                keypress.w = False
            elif event.key == pygame.K_a:
                keypress.a = False
            elif event.key == pygame.K_s:
                keypress.s = False
            elif event.key == pygame.K_d:
                keypress.d = False

    return True

