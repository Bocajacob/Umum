# Python Game Tutorial
# Based on https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

import pygame
from pygame.locals import *
import math

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
acc=[0,0]
arrows=[]

keys = [False, False, False, False]
player_pos = [100, 100]

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")

while 1:
    screen.fill(0)

    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass, (x*100,y*100))
    screen.blit(castle, (0,30))
    screen.blit(castle, (0,135))
    screen.blit(castle, (0,240))
    screen.blit(castle, (0,345))

    mouse_pos = pygame.mouse.get_pos()
    angle_rads = math.atan2(mouse_pos[1] - (player_pos[1] + 32), mouse_pos[0] - (player_pos[0] + 26))
    angle_degrees = 360 - angle_rads * 57.29
    rotated_player = pygame.transform.rotate(player, angle_degrees)
    rotated_pos = (player_pos[0] - rotated_player.get_rect().width / 2, player_pos[1] - rotated_player.get_rect().height / 2)
    screen.blit(rotated_player, rotated_pos)

    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

        if keys[0]:
            player_pos[1] -= 5
        elif keys[2]:
            player_pos[1] += 5
        if keys[1]:
            player_pos[0] -= 5
        elif keys[3]:
            player_pos[0] += 5

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrow_angle = math.atan2(position[1] - (rotated_pos[1] + 32), position[0] - (rotated_pos[0] + 26))
            arrows.append([arrow_angle, rotated_pos[0] + 32, rotated_pos[1] + 32])


