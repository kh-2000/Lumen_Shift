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

            # Außen
            pygame.Rect(0, 0, 1280, 30),
            pygame.Rect(0, 690, 1280, 30),
            pygame.Rect(0, 0, 30, 720),
            pygame.Rect(1250, 0, 30, 720),

            # Oben links
            pygame.Rect(300, 30, 30, 180),

            # Oben Mitte → Tür
            pygame.Rect(650, 30, 30, 120),
            pygame.Rect(650, 220, 30, 70),

            # Oben rechts → Tür
            pygame.Rect(980, 30, 30, 180),

            # Mittlere Wand → Türen
            pygame.Rect(30, 300, 220, 30),
            pygame.Rect(350, 300, 260, 30),
            pygame.Rect(710, 300, 220, 30),
            pygame.Rect(1030, 300, 220, 30),

            # Unten links → Tür
            pygame.Rect(300, 400, 30, 260),

            # Unten Mitte → Tür
            pygame.Rect(650, 330, 30, 130),
            pygame.Rect(650, 540, 30, 120),

            # Unten rechts → Tür
            pygame.Rect(980, 430, 30, 230),

        ]

        self.shadow_walls = [

            # Außen
            pygame.Rect(0, 0, 1280, 30),
            pygame.Rect(0, 690, 1280, 30),
            pygame.Rect(0, 0, 30, 720),
            pygame.Rect(1250, 0, 30, 720),

            # Andere Öffnungen
            pygame.Rect(220, 30, 30, 220),

            pygame.Rect(520, 30, 30, 140),
            pygame.Rect(520, 260, 30, 400),

            pygame.Rect(870, 150, 30, 510),

            # Mittlere Wand → mehrere Lücken
            pygame.Rect(30, 300, 180, 30),
            pygame.Rect(320, 300, 300, 30),
            pygame.Rect(740, 300, 180, 30),

            # Unten
            pygame.Rect(300, 520, 250, 30),
            pygame.Rect(700, 520, 250, 30),

        ]
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