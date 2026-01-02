from constants import *
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        tri = self.triangle()
        pygame.draw.polygon(screen,"white", tri, LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.timer < 0:
            self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) #type: ignore
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(0 - dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(0 - dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()