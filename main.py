import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Playing")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5 #player Speed

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name): #load bg from assets
  image = pygame.image.load(join("assets", "Background", name))
  _, _, width, height = image.get_rect() 
  tiles = [] # create an array
  
  for i in range(WIDTH // width + 1): #check how many tiles need to fill screen
    for j in range(HEIGHT // height + 1):
      pos = (i * width, j * height)
      tiles.append(pos)
      
  return tiles, image

def draw(window, background, bg_image):
  for tile in background:
    window.blit(bg_image, tile)
    
  pygame.display.update()

def main(window):
  clock = pygame.time.Clock()
  background, bg_image = get_background("Yellow.png")
  
  run = True
  while run:
    clock.tick(FPS) #let game run 60FPS
    
    for event in pygame.event.get(): #quit game
      if event.type == pygame.QUIT:
        run = False
        break
      
    draw(window, background, bg_image)    
  pygame.quit()
  quit()

if __name__ == "__main__":
  main(window)