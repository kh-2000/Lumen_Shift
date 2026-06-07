import pygame

from player import Player
from world.World import World

WIDTH = 1280
HEIGHT = 720
FPS = 60
MENU = "menu"
GAME = "game"
PAUSE = "pause"

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Lumen Shift")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = MENU
        self.player = Player(WIDTH // 2,HEIGHT // 2)
        self.world = World()
        self.font = pygame.font.SysFont("arial",40)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if self.state == MENU:
                    if event.key == pygame.K_RETURN:
                        self.state = GAME
                elif self.state == GAME:
                    if event.key == pygame.K_ESCAPE:
                        self.state = PAUSE
                    elif event.key == pygame.K_LSHIFT:
                        self.world.toggle_world()
                elif self.state == PAUSE:
                    if event.key == pygame.K_ESCAPE:
                        self.state = GAME

    def update(self, dt):
        if self.state == GAME:
            self.player.update(dt,self.world.get_walls())

    def draw_menu(self):
        self.screen.fill((20, 20, 20))
        title = self.font.render("LUMEN SHIFT",True,(255, 255, 255))
        start = self.font.render("ENTER → SPIELEN",True,(180, 180, 180))
        self.screen.blit(title,(450, 250))
        self.screen.blit(start,(430, 350))

    def draw_pause(self):
        text = self.font.render("PAUSE",True,(255, 255, 255))
        info = self.font.render("ESC → WEITER",True,(220, 220, 220))
        self.screen.blit(text,(550, 250))
        self.screen.blit(info, (500, 330))

    def draw_game(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        world_text = self.font.render(
            "REALITÄT"
            if self.world.is_reality()
            else "SCHATTENWELT",
            True,
            (60, 150, 255)
            if self.world.is_reality()
            else
            (180, 80, 255))
        self.screen.blit(world_text,(20, 20))

    def draw(self):
        if self.state == MENU:
            self.draw_menu()
        elif self.state == GAME:
            self.draw_game()
        elif self.state == PAUSE:
            self.draw_game()
            self.draw_pause()
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = (self.clock.tick(FPS)/ 1000)
            self.events()
            self.update(dt)
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()