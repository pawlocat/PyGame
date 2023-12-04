import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Playing")

WIDTH, HEIGHT = 1000, 800
FPS = 120
PLAYER_VEL = 10 #player moving speed

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
  COLOR = (255, 0, 0)
  GRAVITY = 1
  def __init__(self, x, y, width, height):
    self.rect = pygame.Rect(x, y, width, height)
    self.x_vel = 0 #player moving speed
    self.y_vel = 0 #player moving speed
    self.mask = None
    self.direction = "left"
    self.animation_count = 0
    self.fall_count = 0
  
  def move(self, dx, dy):
    self.rect.x += dx
    self.rect.y += dy
    
  def move_left(self, vel):
    self.x_vel = -vel
    if self.direction != "left":
      self.direction = "left"
      self.animation_count = 0
      
  def move_right(self, vel):
    self.x_vel = vel  
    if self.direction != "right":
      self.direction = "right"
      self.animation_count = 0
  
  def loop(self, fps):
    self.y_vel += min((1, self.fall_count / fps) * self.GRAVITY)
    self.move(self.x_vel, self.y_vel)
    
    self.fall_count += 1
  
  def draw(self, win):
    pygame.draw.rect(win, self.COLOR, self.rect)
      
def get_background(name): #load bg from assets
  image = pygame.image.load(join("assets", "Background", name))
  _, _, width, height = image.get_rect() 
  tiles = [] # create an array
  
  for i in range(WIDTH // width + 1): #check how many tiles need to fill screen
    for j in range(HEIGHT // height + 1):
      pos = (i * width, j * height)
      tiles.append(pos)
      
  return tiles, image

def draw(window, background, bg_image, player):
  for tile in background:
    window.blit(bg_image, tile)
  
  player.draw(window)
  
  pygame.display.update()

def handle_move(player):
  keys = pygame.key.get_pressed()
  
  player.x_vel = 0
  
  if keys[pygame.K_LEFT]:
    player.move_left(PLAYER_VEL)
  if keys[pygame.K_RIGHT]:
    player.move_right(PLAYER_VEL)

def main(window):
  clock = pygame.time.Clock()
  background, bg_image = get_background("Yellow.png")
  
  player = Player(100, 100, 50, 50)
  run = True
  while run:
    clock.tick(FPS) #let game run 60FPS
    
    for event in pygame.event.get(): #quit game
      if event.type == pygame.QUIT:
        run = False
        break
      
    player.loop(FPS) #60FPS run this def
    handle_move(player)  
    draw(window, background, bg_image, player)    
  pygame.quit()
  quit()

if __name__ == "__main__":
  main(window)