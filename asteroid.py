import pygame  # type: ignore
import random
from constants import *
from circleshape import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            r1 = self.velocity.rotate(random_angle)
            r2 = self.velocity.rotate(0-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = r1 * 1.2
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2.velocity = r2 * 1.2

