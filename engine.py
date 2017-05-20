#!/usr/bin/env python3

import sys
try:
    import android
except ImportError:
    android = None
import pygame
import pygame.gfxdraw
import random
# import pygame.Color
import time
# android = None
pygame.init()
# try:
#     import android
# except ImportError:
#     pass
# if android:
#     android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

try:
    if android:
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
        android.map_key(android.KEYCODE_VOLUME_DOWN,pygame.K_SPACE)
        android.map_key(android.KEYCODE_VOLUME_UP,pygame.K_TAB)
except:
    pass

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
mainfont = pygame.font.Font("./FSEX300-L.ttf",24)
DEBUG = False

engine_version = "1.0"
speed = [2, 2]
black = 0, 0, 0
black = (0x1d,  0x20,  0x21)
mouse_deadzone = 100

gb_black = (0x1d,  0x20,  0x21)  # 1d2021
gb_black2 = (0x7c,  0x6f,  0x64)  # 7c6f64
gb_red = (0xcc,  0x24,  0x1d)  # cc241d
gb_red2 = (0xfb,  0x49,  0x34)  # fb4934
gb_green = (0x98,  0x97,  0x1a)  # 98971a
gb_green2 = (0xb8,  0xbb,  0x26)  # b8bb26
gb_yellow = (0xd7,  0x99,  0x21)  # d79921
gb_yellow2 = (0xfa,  0xbd,  0x2f)  # fabd2f
gb_blue = (0x45,  0x85,  0x88)  # 458588
gb_blue2 = (0x83,  0xa5,  0x98)  # 83a598
gb_magenta = (0xb1,  0x62,  0x86)  # b16286
gb_magenta2 = (0xd3,  0x86,  0x9b)  # d3869b
gb_cyan = (0x68,  0x9d,  0x6a)  # 689d6a
gb_cyan2 = (0x8e,  0xc0,  0x7c)  # 8ec07c
gb_white = (0xd5, 0xc4, 0xa1)
gb_white2 = (0xf9, 0xf5, 0xd7)

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
    tab    =  False


# size = width, height = 320, 240
size = width, height = 800, 480
# size = width, height = 480, 800
# size = width, height = 1024, 768
# size = width, height = 1920, 1080
# screen = pygame.display.set_mode(size,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
# screen = pygame.display.set_mode(size,pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
screen = pygame.display.set_mode(size,pygame.DOUBLEBUF | pygame.HWSURFACE)
screen.set_alpha(None)             # Engine is so simple, it does not use an alhpa channel
# pygame.mouse.set_visible(False) # invisible mouse
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
    r = int(random.randrange(255))
    g = int(random.randrange(255))
    b = int(random.randrange(255))
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

def dropoff_color(color,ratio):
    r,g,b = map(lambda x:x*ratio,color)
    return (r,g,b)

def draw_polygon(points,color,topdown,outline=False):
    # pygame.draw.polygon(screen, map((lambda width,height:(int(width/2+x), int(height/2+y))),points), color)
    if topdown:
        pygame.draw.polygon(screen, gb_black, list([(int(width/2.0+x), int(height/2.0+y)) for x,y in points]), 0)
        pygame.draw.polygon(screen, gb_black2, list([(int(width/2.0+x), int(height/2.0+y)) for x,y in points]), 1)
    else:
        pygame.draw.polygon(screen, color, list([(int(width/2.0+x), int(height/2.0+y)) for x,y in points]), 0)
        if outline:
            pygame.draw.polygon(screen, outline, list([(int(width/2.0+x), int(height/2.0+y)) for x,y in points]), 1)



def draw_column(x,y_top,y_bottom,color):
    # color = fog_color(color,wall_angle)
    y_top = min(y_top,height)
    y_bottom = max(y_bottom,-height)
    try:
        if DEBUG:
            pygame.gfxdraw.line(screen, int(width/2+x), int(height/2+y_top), int(width/2+x), int(height/2+y_bottom), randomcolor())
            pygame.display.flip()
            time.sleep(0.001)
        pygame.gfxdraw.line(screen, int(width/2+x), int(height/2+y_top), int(width/2+x), int(height/2+y_bottom), color)
        # if DEBUG:
        # pygame.gfxdraw.pixel(screen, int(width/2+x), int(height/2+y_top), (0x1d,  0x20,  0x21,  255))
        # pygame.gfxdraw.pixel(screen, int(width/2+x), int(height/2+y_bottom), (0x1d,  0x20,  0x21,  255))
    except:
        pass
        # pygame.gfxdraw.pixel(screen, int(width/2+x), int(height/2+y_top), black)
    # pygame.gfxdraw.pixel(screen, int(width/2+x), int(height/2+y_bottom), black)

def draw_triangle(x1,y1,x2,y2,x3,y3,color=white):
    pygame.draw.polygon(screen, color,
                        [[int(width/2+x1), int(height/2+y1)],
                         [int(width/2+x2), int(height/2+y2)],
                         [int(width/2+x3), int(height/2+y3)]])


clock = pygame.time.Clock()

def engine_step(keypress=keypress(),framerate=60):
    global screen,height,width,DEBUG
    clock.tick(framerate)
    pygame.display.flip()
    # screen.fill(black)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # keypress.space = True
        elif event.type == pygame.MOUSEBUTTONUP:
            keypress.left = False
            keypress.right = False
            keypress.up = False
            keypress.down = False
            keypress.space = False
            keypress.a = False
            keypress.d = False
        elif event.type == pygame.VIDEORESIZE:
            width,height=event.size
            screen = pygame.display.set_mode(event.size)
        elif event.type == pygame.KEYDOWN:
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
            elif event.key == pygame.K_TAB:
                keypress.tab = True
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
            elif event.key == pygame.K_TAB:
                keypress.tab = False
        if pygame.mouse.get_pressed()[0]:
            try:
                mx,my = pygame.mouse.get_pos()
                cmx, cmy = mx - width//2,my - height//2
                keypress.a = cmx < -mouse_deadzone and cmy > mouse_deadzone
                keypress.d = cmx > mouse_deadzone and cmy > mouse_deadzone
                keypress.tab = cmx < -mouse_deadzone and cmy < -mouse_deadzone
                keypress.left = cmx < -mouse_deadzone and cmy < mouse_deadzone and cmy > -mouse_deadzone
                keypress.right = cmx > mouse_deadzone and cmy < mouse_deadzone and cmy > -mouse_deadzone
                keypress.up = cmy < -mouse_deadzone and cmx < mouse_deadzone and cmx > -mouse_deadzone
                keypress.down = cmy > mouse_deadzone and cmx < mouse_deadzone and cmx > -mouse_deadzone
                if cmx > -mouse_deadzone and\
                   cmx < mouse_deadzone and\
                   cmy > -mouse_deadzone and\
                   cmy < mouse_deadzone:
                    keypress.space = True
                else:
                    keypress.space = False
            except AttributeError:
                pass

    return True

