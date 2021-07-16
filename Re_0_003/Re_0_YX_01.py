import sys
import math
import pygame
from pygame.locals import *


'''

white = 255, 255, 255
blue = 0, 0, 255
pygame.init()   # 初始化
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
textImage = myfont.render('Hello Pygame', True, white)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()


''' # 创建了一个  窗口 可持续 显示 并有用户反应

'''

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Drawing Circles')
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))

    # draw a circle
    color = 255,255,0
    position = 300,250 # 位置
    radius = 100  # 大小
    width = 10  # 线条的 粗细
    pygame.draw.circle(screen,color,position,radius,width)

    pygame.display.update()

''' # 绘制园

'''

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Drawing Rectangles')
pos_x = 300; pos_y = 250
vel_x = 2; vel_y = 1
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))

    # move the recatangle
    pos_x += vel_x
    pos_y += vel_y

    # keep rectangle on the screen
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    # draw the rectangle
    color = 255,255,0
    width = 0
    pos = pos_x,pos_y,100,100
    pygame.draw.rect(screen,color,pos,width)
    pygame.display.update()

''' # 绘制 矩阵

'''

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill((0,80,0))

    # draw the line
    color = 100,255,200
    width = 8
    pygame.draw.line(screen,color,(100,100),(500,400),width)

    pygame.display.update()

''' # 绘制 直线

'''

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()

    screen.fill((0,0,200))

    # draw the acs
    color = 255,0,255
    position = 200,150,200,200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    width = 8
    pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
    pygame.display.update()

''' # 绘制 曲线

'''

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("The Pie Game -Press 1,2,3,4")
myfont = pygame.font.Font(None,60)

color = 200,80,60
width = 4
x = 300; y = 250
radius = 200
position = x - radius, y - radius,radius*2, radius*2

piece1 = False; piece2 = False; piece3 = False; piece4 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True

    # clear the screen
    screen.fill((0,0,200))

    # draw the four numbers
    textImg1 = myfont.render("1", True, color)
    screen.blit(textImg1, (x+radius/2-20, y-radius/2))

    textImg2 = myfont.render("2", True, color)
    screen.blit(textImg2, (x-radius/2, y-radius/2))

    textImg3 = myfont.render("3", True, color)
    screen.blit(textImg3, (x-radius/2, y+radius/2-20))

    textImg4 = myfont.render("4", True, color)
    screen.blit(textImg4, (x+radius/2-20, y+radius/2-20))

    # should the pieces be draen?
    if piece1:
        strat_angle = math.radians(0)
        end_angle = math.radians(90)
        pygame.draw.arc(screen, color, position, strat_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y-radius), width)
        pygame.draw.line(screen, color, (x, y), (x+radius, y),width)

    if piece2:
        strat_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen, color, position, strat_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y - radius), width)
        pygame.draw.line(screen, color, (x, y), (x - radius, y), width)

    if piece3:
        strat_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen, color, position, strat_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x-radius, y), width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius),width)

    if piece4:
        strat_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen, color, position, strat_angle, end_angle, width)
        pygame.draw.line(screen, color, (x, y), (x, y + radius), width)
        pygame.draw.line(screen, color, (x, y), (x + radius, y),width)

    # is the pie finished
    if piece1 and piece2 and piece3 and piece4:
        color = 0,255,0

    pygame.display.update()

''' # Pie 游戏
















