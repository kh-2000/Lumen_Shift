import pygame
from player import Player
from world.World import World
from enemy import Enemy
from menu import Menu

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
        self.enemy = Enemy()
        self.game_over = False
        self.font = pygame.font.SysFont("arial",40)
        self.menu = Menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.state == MENU:
                self.menu.handle_event(event,self)
            elif self.state == GAME:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = PAUSE
                    elif (event.key == pygame.K_LSHIFT):
                        self.world.toggle_world()
            elif self.state == PAUSE:
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        self.state = GAME

    def update(self, dt):
        if self.state == GAME:
            self.player.update(dt, self.world.get_walls())
            self.enemy.update(dt, self.world)
            if self.enemy.touches_player(self.player):
                self.game_over = True
                self.state = MENU

    def draw_menu(self):
        self.menu.update()
        self.menu.draw(self.screen)

    def draw_pause(self):
        text = self.font.render("PAUSE",True,(255, 255, 255))
        info = self.font.render("ESC → WEITER",True,(220, 220, 220))
        self.screen.blit(text,(550, 250))
        self.screen.blit(info, (500, 330))

    def draw_game(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        self.enemy.draw(self.screen, self.world)
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
        self.menu.draw_ui(self.screen, self.world)

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