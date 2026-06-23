# KI-Anfang
# KI: ChatGPT
# prompt:
# Mehrere zufällige Batterien erzeugen
# KI-Ende

import pygame
import random


class BatteryManager:

    def __init__(self, world):

        self.batteries = []

        self.spawn_all(
            world
        )

    def spawn_all(
            self,
            world):

        self.batteries.clear()

        for i in range(3):

            while True:

                x = random.randint(
                    120,
                    1100
                )

                y = random.randint(
                    120,
                    600
                )

                rect = pygame.Rect(
                    x,
                    y,
                    35,
                    35
                )

                blocked = False

                for wall in world.shadow_walls:

                    if rect.colliderect(
                            wall):

                        blocked = True

                for battery in self.batteries:

                    if rect.colliderect(
                            battery):

                        blocked = True

                if not blocked:

                    self.batteries.append(
                        rect
                    )

                    break

    def collect(
            self,
            player,
            world,
            carrying):

        if world.is_reality():
            return False

        if carrying:
            return False

        keys = pygame.key.get_pressed()

        if not keys[pygame.K_e]:
            return False

        for battery in self.batteries:

            if player.rect.colliderect(
                    battery):
                self.batteries.remove(
                    battery
                )

                return True

        return False

    def draw(
            self,
            screen,
            world):

        if world.is_reality():

            return

        for battery in self.batteries:

            pygame.draw.rect(

                screen,

                (
                    0,
                    220,
                    255
                ),

                battery,

                border_radius=8

            )

    def all_collected(self):

        return (
            len(
                self.batteries
            )
            ==
            0
        )