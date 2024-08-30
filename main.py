import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  Shot.containers = (shots, updatable, drawable)

  asteroid_field = AsteroidField()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    screen.fill(color="black")

    for obj in updatable:
      obj.update(dt)

    for obj in drawable:
      obj.draw(screen)
    
    for obj in asteroids:
      if obj.is_colliding(player):
        print("Game over!")
        exit()


    pygame.display.flip()
    dt = clock.tick(60)/1000

if __name__ == "__main__":
  main()