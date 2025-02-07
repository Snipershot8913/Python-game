import pygame
import math 
import random 
pygame.init()
screen = pygame.display.set_mode((1000,500),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
#def var and funtions
player_X = 0
player_Y = 0
hidden = []
seen = []
#main run
while running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  listrun=0
  if keys[pygame.K_w]:
     player_Y += 1
  if keys[pygame.K_s]:
     player_Y -=1
  if keys[pygame.K_a]:
     player_X +=1
  if keys[pygame.K_d]:
     player_X -=1
  print(player_X "," player_Y)
  
  
  

