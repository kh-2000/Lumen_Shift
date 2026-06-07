import pygame

class World:
    REALITY = "reality"
    SHADOW = "shadow"
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self):
        self.current_world = self.REALITY
        self.reality_image = pygame.image.load("assets/weiss.png").convert()
        self.shadow_image = pygame.image.load("assets/schwarz.png").convert()
        self.reality_image = pygame.transform.scale(self.reality_image,(self.WIDTH, self.HEIGHT))
        self.shadow_image = pygame.transform.scale(self.shadow_image,(self.WIDTH, self.HEIGHT))

        self.reality_walls = [
            pygame.Rect(0, 0, 1280, 30),
            pygame.Rect(0, 690, 1280, 30),
            pygame.Rect(0, 0, 30, 720),
            pygame.Rect(1250, 0, 30, 720)]# den bildschrirand werde ich genauer an die wände anpsassen


        self.shadow_walls = [
            pygame.Rect(0, 0, 1280, 30),
            pygame.Rect(0, 690, 1280, 30),
            pygame.Rect(0, 0, 30, 720),
            pygame.Rect(1250, 0, 30, 720)]# den bildschrirand werde ich genauer an die wände anpsassen

    def toggle_world(self):
        if self.current_world == self.REALITY:
            self.current_world = self.SHADOW
        else:
            self.current_world = self.REALITY

    def get_walls(self):
        if self.current_world == self.REALITY:
            return self.reality_walls
        return self.shadow_walls

    def draw(self, screen):
        if self.current_world == self.REALITY:
            screen.blit(self.reality_image, (0, 0))
            walls = self.reality_walls
        else:
            screen.blit(self.shadow_image, (0, 0))
            walls = self.shadow_walls

        for wall in walls:
            pygame.draw.rect(screen,(255, 0, 0), wall,2) #damit ich die wände erkenne, das entferne ich noch

    def is_reality(self):
        return self.current_world == self.REALITY