import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Playing")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5 #player Speed

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
  clock = pygame.time.Clock()
  
  run = True
  while run:
    clock.tick(FPS) #let game run 60FPS
    
    for event in pygame.event.get(): #quit game
      if event.type == pygame.QUIT:
        run = False
        break
      
  pygame.quit()
  quit()

if __name__ == "__main__":
  main(window)