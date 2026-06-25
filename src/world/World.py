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
            pygame.Rect(0, 60, 1280, 30),
            pygame.Rect(10, 600, 1280, 30),
            pygame.Rect(0, 0, 30, 720),
            pygame.Rect(1230, 0, 30, 720),

            pygame.Rect(430, 30, 20, 290 ),
            pygame.Rect(510, 30, 20, 280),

            pygame.Rect(660, 30, 20, 120),
            pygame.Rect(660, 240, 20, 70),

            pygame.Rect(710, 30, 20, 120),
            pygame.Rect(710, 240, 20, 70),

            pygame.Rect(970, 30, 20, 200),
            pygame.Rect(510, 30, 20, 280),
            pygame.Rect(430, 420, 20, 270),
            pygame.Rect(740, 420, 20, 270),
            pygame.Rect(820, 270, 20, 70),

            pygame.Rect(30, 280, 230, 20),
            pygame.Rect(330, 280, 100, 20),
            pygame.Rect(890, 210, 260, 20),
            pygame.Rect(820, 270, 80, 20),
            pygame.Rect(750, 430, 210, 20),
            pygame.Rect(1100, 430, 100, 20),

            # # Oben links
            # pygame.Rect(300, 30, 30, 180),
            #
            # # Oben Mitte → Tür
            # pygame.Rect(650, 30, 30, 120),
            # pygame.Rect(650, 220, 30, 70),
            #
            # # Oben rechts → Tür
            # pygame.Rect(980, 30, 30, 180),
            #
            # # Mittlere Wand → Türen
            # pygame.Rect(30, 300, 220, 30),
            # pygame.Rect(350, 300, 260, 30),
            # pygame.Rect(710, 300, 220, 30),
            # pygame.Rect(1030, 300, 220, 30),
            #
            # # Unten links → Tür
            # pygame.Rect(300, 400, 30, 260),
            #
            # # Unten Mitte → Tür
            # pygame.Rect(650, 330, 30, 130),
            # pygame.Rect(650, 540, 30, 120),
            #
            # # Unten rechts → Tür
            # pygame.Rect(980, 430, 30, 230),

        ]

        self.shadow_walls = [

            pygame.Rect(0, 30, 1280, 30),
            pygame.Rect(10, 600, 1280, 30),
            pygame.Rect(0, 0, 30, 720),
            pygame.Rect(1230, 0, 30, 720),

            pygame.Rect(140, 110, 20, 290),
            pygame.Rect(530, 30, 20, 190),
            pygame.Rect(660, 30, 20, 280),
            pygame.Rect(970, 30, 20, 100),
            pygame.Rect(650, 420, 20, 270),
            pygame.Rect(900, 280, 67, 80),
            pygame.Rect(340, 390, 70, 2700),

            pygame.Rect(30, 280, 200, 20),
            pygame.Rect(280, 280, 300, 20),
            pygame.Rect(1000, 110, 260, 20),
            pygame.Rect(700, 310, 130, 20),
            pygame.Rect(1130, 275, 100, 20),
            pygame.Rect(1130, 330, 100, 100),


            # # Außen
            # pygame.Rect(0, 0, 1280, 30),
            # pygame.Rect(0, 690, 1280, 30),
            # pygame.Rect(0, 0, 30, 720),
            # pygame.Rect(1250, 0, 30, 720),
            #
            # # Andere Öffnungen
            # pygame.Rect(220, 30, 30, 220),
            #
            # pygame.Rect(520, 30, 30, 140),
            # pygame.Rect(520, 260, 30, 400),
            #
            # pygame.Rect(870, 150, 30, 510),
            #
            # # Mittlere Wand → mehrere Lücken
            # pygame.Rect(30, 300, 180, 30),
            # pygame.Rect(320, 300, 300, 30),
            # pygame.Rect(740, 300, 180, 30),
            #
            # # Unten
            # pygame.Rect(300, 520, 250, 30),
            # pygame.Rect(700, 520, 250, 30),

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