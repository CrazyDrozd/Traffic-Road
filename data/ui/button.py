"""Abstract base button with hover and click support."""

import pygame

from abc import abstractmethod
from typing import Tuple

from data.interfaces.sprite_interfaces import Drawable
from data.interfaces.event_listeners import ClickListener, HoverListener


# ==================== ИНТЕРФЕЙС КНОПКИ ====================
class Button(Drawable, ClickListener, HoverListener):
    """
    Абстрактный класс кнопки
    
    Hierarchy:
        Советуется располагать в наследовании первым ради чёткого понимания и структурирования.

    Methods:
        >>> draw(self, screen: pygame.Surface)
        
        >>> on_hover(self, mouse_pos: Tuple[int, int])

        >>> on_click(self, mouse_pos: Tuple[int, int], button: int)

        >>> click (self) —— абстрактный метод

    Examples:
        >>> DebugButton(Button)
    """
    def __init__(self, x: int, y: int, width: int, height: int, text: str):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (0, 0, 0)
        self.hover_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 24)
        self.is_hovered = False

    def draw(self, screen: pygame.Surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def on_hover(self, mouse_pos: Tuple[int, int]):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def on_click(self, mouse_pos: Tuple[int, int], button: int):
        if button == 1 and self.rect.collidepoint(mouse_pos):
            self.click()

    @abstractmethod
    def click(self):
        pass