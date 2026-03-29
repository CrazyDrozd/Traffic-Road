"""Concrete button to toggle debug mode, and a debug overlay that shows info and toggles with F3."""

import pygame

from data.config import GameConfig

from data.interfaces.sprite_interfaces import Drawable
from data.interfaces.event_listeners import KeyListener

from data.ui.button import Button


# ==================== КЛАСС КНОПКИ ДЕБАГА ====================
class DebugButton(Button):
    def __init__(self, x: int, y: int, config: GameConfig):
        super().__init__(x, y, 100, 40, "Дебаг")
        self.config = config

    def click(self):
        self.config.DEBUG = not self.config.DEBUG


# ==================== ДЕБАГ ОВЕРЛЕЙ ====================
class DebugOverlay(Drawable, KeyListener):
    def __init__(self, config: GameConfig, target_button: Button, offset_x: int = 10, offset_y: int = 50):
        self.config = config
        self.target_button = target_button
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.font = pygame.font.Font(None, 22)
        self.bg_color = (0, 0, 0, 220)
        self.text_color = (255, 255, 255)
        self.surface = pygame.Surface((280, 180), pygame.SRCALPHA)

    def on_key_down(self, key: int):
        if key == pygame.K_F3:
            self.config.DEBUG = not self.config.DEBUG

    def on_key_up(self, key: int):
        pass

    def draw(self, screen: pygame.Surface):
        if not self.config.DEBUG:
            return

        self.surface.fill(self.bg_color)

        lines = [
            f"=== DEBUG INFO ===",
            f"Version: {self.config.VERSION}",
            f"F3: Переключить дебаг"
        ]

        y_offset = 5
        for line in lines:
            text = self.font.render(line, True, self.text_color)
            self.surface.blit(text, (5, y_offset))
            y_offset += 18

        x = self.target_button.rect.x + self.offset_x
        y = self.target_button.rect.y + self.offset_y
        screen.blit(self.surface, (x, y))