import math
import random
import time
import pygame

# Variables
A = 0
B = 0
ball_x = 2 * random.choice((1, -1))
ball_y = 2 * random.choice((1, -1))
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0,0,255)
ballx = 300
bally = 300
ballR = 10
point = 0
prx = 560
pry = 10
plx = 20
ply = 300
ly_change = 0
ry_change = 0
# Initialization
pygame.init()
win = pygame.display.set_mode((600, 600), )


# Functions
def motion():
    global ballx, bally
    ballx += ball_x
    bally += ball_y


font = pygame.font.SysFont("comicsansms", 50)

# Loop
run = True
while run:
    caption = pygame.display.set_caption("Pong by Aadil ")
    win.fill(black)
    paddleLeft = pygame.draw.rect(win, green, (prx, pry, 20, 80), 0)
    paddleRight = pygame.draw.rect(win, green, (plx, ply, 20, 80), 0)
    ball = pygame.draw.circle(win, white, (ballx, bally), ballR, 0)

    # border
    border1 = pygame.draw.rect(win, white, (15, 0, 2, 600), 0)
    border2 = pygame.draw.rect(win, white, (0, 15, 600, 2), 0)
    border3 = pygame.draw.rect(win, white, (585, 0, 2, 600), 0)
    border4 = pygame.draw.rect(win, white, (0, 585, 600, 2), 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ly_change -= 5
            if event.key == pygame.K_s:
                ly_change += 5
            if event.key == pygame.K_UP:
                ry_change -= 5
            if event.key == pygame.K_DOWN:
                ry_change += 5
        if event.type == pygame.KEYUP:
            ly_change = 0
            ry_change = 0
    pry += ry_change
    ply += ly_change
    if pry <= 15:
        pry = 15
    if pry >= 505:
        pry = 505
    if ply <= 15:
        ply = 15
    if ply >= 505:
        ply = 505
    if bally <= 27:
        bally = 27
        ball_y *= -1
    if bally >= 573:
        bally = 573
        ball_y *= -1
    if ballx <= 40:
        if bally >= ply and bally <= ply + 80:
            ballx = 40
            ball_x *= -1
        else:
            ballx = 300
            bally = 300
            ball_x = random.choice((1, -1))
            ball_y = random.choice((1, -1))
            B += 1
    if ballx >= 560:
        if bally >= pry and bally <= pry + 80:
            ballx = 560
            ball_x *= -1
        else:
            ballx = 300
            bally = 300
            ball_x = random.choice((1, -1))
            ball_y = random.choice((1, -1))
            A += 1
    if A ==10 or B ==10:
        run = False
    text = font.render("A: "+str(A)+"         B: "+str(B), True, blue)
    win.blit(text,(130,10))
    motion()
    pygame.time.delay(8)
    pygame.display.update()
if A == 10:
    finalText = font.render("A wins!!",True, blue)
    win.blit(finalText, (200, 260))
elif B == 10:
    finalText = font.render("B wins!!",True, blue)
    win.blit(finalText, (200, 260))
else:
    pass

pygame.display.update()
time.sleep(3)
