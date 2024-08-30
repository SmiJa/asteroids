import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  containers =()
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.position = pygame.Vector2(x, y)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      random_angle = random.uniform(20, 50)
      pos_angle = self.velocity.rotate(random_angle)
      neg_angle = self.velocity.rotate(-random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid_1.velocity = pos_angle
      asteroid_2.velocity = neg_angle

