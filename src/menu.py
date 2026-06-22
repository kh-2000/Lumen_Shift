# KI-Anfang
# KI: ChatGPT
# prompt:
# Menü für mein Lumen Shift projekt mit Start, Speichern, Beenden mit pygame


import pygame
import json
import os


class Menu:

    def __init__(self):

        self.font = pygame.font.SysFont(
            "arial",
            50
        )

        self.title_font = pygame.font.SysFont(
            "arial",
            90
        )

        self.options = [

            "SPIELEN",

            "SPEICHERN",

            "LADEN",

            "BEENDEN"

        ]

        self.selected = 0

        self.message = ""

        self.message_timer = 0

        try:

            self.background = pygame.image.load(
                "assets/menu.png"
            ).convert()

            self.background = pygame.transform.scale(
                self.background,
                (1280, 720)
            )

        except:

            self.background = None

    def handle_event(
            self,
            event,
            game):

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:

            self.selected -= 1

            if self.selected < 0:
                self.selected = (
                    len(
                        self.options
                    )
                    - 1
                )

        elif event.key == pygame.K_DOWN:

            self.selected += 1

            if (
                self.selected
                >=
                len(
                    self.options
                )
            ):

                self.selected = 0

        elif event.key == pygame.K_RETURN:

            if self.selected == 0:

                game.state = "game"

            elif self.selected == 1:

                self.save_game(
                    game
                )

            elif self.selected == 2:

                self.load_game(
                    game
                )

            elif self.selected == 3:

                game.running = False

    def save_game(
            self,
            game):

        data = {

            "x":
            game.player.rect.x,

            "y":
            game.player.rect.y,

            "world":
            game.world.current_world

        }

        with open(
                "savegame.json",
                "w"
        ) as file:

            json.dump(
                data,
                file
            )

        self.message = "GESPEICHERT"

        self.message_timer = 180

    def load_game(
            self,
            game):

        if not os.path.exists(
                "savegame.json"
        ):

            self.message = "KEIN SAVE"

            self.message_timer = 180

            return

        with open(
                "savegame.json",
                "r"
        ) as file:

            data = json.load(
                file
            )

        game.player.rect.x = (
            data["x"]
        )

        game.player.rect.y = (
            data["y"]
        )

        game.world.current_world = (
            data["world"]
        )

        self.message = "GELADEN"

        self.message_timer = 180

    def update(self):

        if (
                self.message_timer
                >
                0
        ):

            self.message_timer -= 1

    def draw(
            self,
            screen):

        if self.background:

            screen.blit(
                self.background,
                (0, 0)
            )

        else:

            screen.fill(
                (
                    10,
                    10,
                    10
                )
            )

        title = self.title_font.render(

            "LUMEN SHIFT",

            True,

            (
                255,
                255,
                255
            )

        )

        screen.blit(
            title,
            (
                330,
                140
            )
        )

        y = 300

        for i, option in enumerate(
                self.options):

            color = (
                180,
                180,
                180
            )

            if (
                    i
                    ==
                    self.selected
            ):

                color = (
                    255,
                    220,
                    0
                )

            text = self.font.render(

                option,

                True,

                color

            )

            screen.blit(
                text,
                (
                    480,
                    y
                )
            )

            y += 90

        if (
                self.message_timer
                >
                0
        ):

            msg = self.font.render(

                self.message,

                True,

                (
                    0,
                    255,
                    100
                )

            )

            screen.blit(
                msg,
                (
                    450,
                    620
                )
            )

    def draw_ui(
            self,
            screen,
            world):

        text = self.font.render(

            "REALITÄT"
            if world.is_reality()
            else "SCHATTENWELT",

            True,

            (
                60,
                150,
                255
            )

            if world.is_reality()

            else

            (
                180,
                80,
                255
            )

        )

        screen.blit(
            text,
            (
                20,
                20
            )
        )
        #KI Ende
        #Ich habe das nur zum testen gebraucht und da chen das noch nciht machen konnta habe ich eien smit KI erstellt,
        #also wie eine skizze, chen macht es dann richtig