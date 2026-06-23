import pygame


class LightStation:

    def __init__(self):

        self.rect = pygame.Rect(
            120,
            540,
            140,
            120
        )

        self.loaded = 0
        self.goal = 3

    def try_insert(
            self,
            player,
            carrying,
            world):

        # Nur Realität
        if not world.is_reality():
            return False

        # Spieler muss Batterie tragen
        if not carrying:
            return False

        # Spieler berührt Station
        if player.rect.colliderect(
                self.rect):

            self.loaded += 1

            return True

        return False

    def finished(self):

        return self.loaded >= self.goal

    def draw(
            self,
            screen):

        pygame.draw.rect(
            screen,
            (255, 240, 100),
            self.rect,
            border_radius=10
        )

        font = pygame.font.SysFont(
            "arial",
            32
        )

        text = font.render(
            f"{self.loaded}/3",
            True,
            (0, 0, 0)
        )

        screen.blit(
            text,
            (
                self.rect.x + 35,
                self.rect.y + 35
            )
        )