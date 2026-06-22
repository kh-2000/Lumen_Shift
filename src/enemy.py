import pygame

class Enemy:
    def __init__(self):
        self.size = 80
        self.rect = pygame.Rect(180, 150, self.size, self.size)

        # Wege vomm monster
        self.points = [
            (180, 150),
            (900, 150),
            (900, 500),
            (350, 500),
            (350, 250)]
        self.target = 1

    def update(self, dt, world):
        if world.is_reality():
            speed = 90
        else:
            speed = 220
        tx, ty = self.points[self.target]
        dx = tx - self.rect.centerx
        dy = ty - self.rect.centery
        distance = (dx**2 + dy**2) ** 0.5

        if distance > 5:
            self.rect.x += (dx / distance) * speed * dt
            self.rect.y += (dy / distance) * speed * dt
        else:
            self.target += 1
            if self.target >= len(
                    self.points):
                self.target = 0

    def touches_player(self, player):
        return self.rect.colliderect(
            player.rect)

    def draw(self, screen, world):
        color = (120, 120, 120)

        if not world.is_reality():
            color = (160, 0, 200)
        pygame.draw.rect(screen, color, self.rect, border_radius=20)