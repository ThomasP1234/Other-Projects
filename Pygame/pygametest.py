import pygame
import time
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Flappy Bird")

icon = pygame.image.load('Game Art\\icon.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('Game Art\\player.png')
playerX = 100
playerY = 190

cloudlst = ["Game Art\\cloud-01.png", "Game Art\\cloud-02.png", "Game Art\\cloud-03.png"]
chosencloudlist = []
cloudX = [20, 120, 170, 320, 500, 650, 710]
cloudY = []
cloudImg = []

landImg = pygame.image.load('Game Art\\land.png')
landX = 0
landY = 0

pipe1Img = pygame.image.load('Game Art\\Obstacle-01\\pipe1.png')
pipe1X = 600
pipe1Y = 280

pipe2Img = pygame.image.load('Game Art\\Obstacle-01\\pipe2.png')
pipe2X = pipe1X
pipe2Y = 0

def clouds():
    if len(chosencloudlist) == 0:
        for i in range(7):
            chosencloudlist.append(random.choice(cloudlst))
        for cloud in chosencloudlist:
            cloudY.append(random.choice(range(10, 80)))
            cloudImg.append(pygame.image.load(cloud))
    for i in range(len(chosencloudlist)):
        screen.blit(cloudImg[i], (cloudX[i], cloudY[i]))

def land():
    screen.blit(landImg, (landX, landY))

def pipe():
    global pipe1X
    global pipe2X
    screen.blit(pipe1Img, (pipe1X, pipe1Y))
    screen.blit(pipe2Img, (pipe2X, pipe2Y))

    if pipe1X < -100:
        pipe1X = 900
    pipe1X -= 2
    pipe2X = pipe1X

def player():
    screen.blit(playerImg, (playerX, playerY))

def iscollision(playerX, playerY, pipeXcenter, pipeYcenter):
    global running
    if (playerX + 32) - (pipeXcenter) < 50 and (playerX + 32) - (pipeXcenter) > 0:
        if (playerY + 22) - (pipeYcenter) < 85 and (playerY + 22) - (pipeYcenter) > 0:
            running = False

running = True
while running:
    screen.fill((0, 191, 255))
    clouds()
    land()

    pipe()

    pipe1Xcenter = pipe1X + 50
    pipe1Ycenter = pipe1Y + 85

    pipe2Xcenter = pipe2X + 50
    pipe2Ycenter = pipe2Y + 85

    # print(pipe1Xcenter, pipe1Ycenter, "      ",pipe2Xcenter, pipe2Ycenter)
    # print(playerX + 32, playerY + 22)
    iscollision(playerX, playerY, pipe1Xcenter, pipe1Ycenter)
    iscollision(playerX, playerY, pipe2Xcenter, pipe2Ycenter)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY -= 50

    if playerY > 365:
        running = False
        # playerY = 190

    if playerY < 0:
        playerY = 0

    playerY += 2
    player()

    pygame.display.update()
    time.sleep(0.01)