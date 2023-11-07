import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
W = 960
H = 720

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Hello World")


def ballRestart():
    global ballX,ballY,timer

    ballX = 7* random.choice((-1,1))
    ballY = 7*random.choice((-1,1))

    ball.center = (W/2,H/2)
    player.topleft = W-20,H/2
    opponent.topleft = 20,H/2
    

def oppAnimation():
    oppSpeed = random.choice(list(range(3,7)))
    if opponent.top <= ball.y:
        opponent.top += oppSpeed
    if opponent.top >= ball.y:
        opponent.bottom -= oppSpeed
    if opponent.top <= 0:
        opponent.top =0
    if opponent.bottom >= H:
        opponent.bottom = H

def playerAnimation():
    player.y += playerSpeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= H:
        player.top = H-player.height

def ballAnimation():
    global ballX,ballY,pScore,oScore,timer
    ball.x+=ballX
    ball.y+=ballY
    if ball.top<=0 or ball.bottom>=H:
        ballY*=-1
    if ball.left<=0:
        pScore+=1
        ball.x,ball.y = (W/2-15,H/2-15)
        ballX,ballY = 0,0
    if ball.right>=W:
        oScore+=1
        ball.x,ball.y = 0,0
        ballX,ballY = 0,0
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballX*=-1

ball = pygame.Rect(W/2-15,H/2-15,30,30)
player = pygame.Rect(W-20,H/2-70,10,140)
opponent = pygame.Rect(20,H/2-70,10,140)

pScore = 0
oScore = 0

gFont = pygame.font.Font("freesansbold.ttf",32)





ballX,ballY = 7,7
playerSpeed = 0
oppSpeed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7
        if event.type == pygame.MOUSEBUTTONUP:
            ballRestart()
    
    ballAnimation()
    playerAnimation()
    oppAnimation()

    screen.fill('grey12')

    pygame.draw.ellipse(screen,"white",ball)
    pygame.draw.rect(screen,"white",player)
    pygame.draw.rect(screen,"white",opponent)
    pygame.draw.aaline(screen,"white",(W/2,0),(W/2,H))

    pText = gFont.render(f'{pScore}',False,'white')
    screen.blit(pText,(505,350))
    oText = gFont.render(f'{oScore}',False,'white')
    screen.blit(oText,(440,350))

    pygame.display.flip()
    clock.tick(60)
