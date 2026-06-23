import pygame


class Player:
    def __init__(self, x, y):
        self.speed = 140
        self.image = pygame.image.load("assets/sprite_player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(60, 60))
        self.rect = self.image.get_rect(center=(x, y))

    def move(self, dt, walls):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_a]:
            dx -= self.speed * dt
        if keys[pygame.K_d]:
            dx += self.speed * dt
        if keys[pygame.K_w]:
            dy -= self.speed * dt
        if keys[pygame.K_s]:
            dy += self.speed * dt
        self.rect.x += dx

        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                if dx < 0:
                    self.rect.left = wall.right
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall):
                if dy > 0:
                    self.rect.bottom = wall.top
                if dy < 0:
                    self.rect.top = wall.bottom
            # NICHT AUS DEM BILDSCHIRM
        self.rect.left = max(
            30,
            self.rect.left
        )

        self.rect.right = min(
            1280,
            self.rect.right
        )

        self.rect.top = max(
            30,
            self.rect.top
        )

        self.rect.bottom = min(
            720,
            self.rect.bottom
        )

    def update(self, dt, walls):
        self.move(dt, walls)

    def draw(self, screen):
        screen.blit(self.image,self.rect)