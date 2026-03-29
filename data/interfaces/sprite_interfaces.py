"""Sprite Interfaces: Drawable, Updatable."""

import pygame
from abc import ABC, abstractmethod


# ==================== ОТРИСОВЫВАЕМЫЙ СПРАЙТ ====================
class Drawable(ABC):
    """
    Абстрактный класс, обозначающий, что последующие классы, наследующие основной метод:
        —— Обладают свойством быть прорисованы на экране.

    Один из двух интерфейсов спрайтов:
        >>> Drawable(ABC)

        >>> Updatable(ABC)
    
    Hierarchy:
        Советуется располагать в наследовании первым ради чёткого понимания и структурирования.

    Methods:
        >>> draw(self, screen: pygame.Surface)

    Examples:
        >>> Button(Drawable, ClickListener, HoverListener, ABC)

        >>> Road(Drawable)

        >>> TrafficLight(Drawable, Updatable)
    """
    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass


# ==================== ОБНОВЛЯЕМЫЙ СПРАЙТ ====================
class Updatable(ABC):
    """
    Абстрактный класс спрайта, обозначающий, что последующие классы, наследующие основной метод:
        —— Обладают свойством обновлять самих себя на экране.

    Один из двух интерфейсов спрайтов:
        >>> Drawable(ABC)

        >>> Updatable(ABC)

    Hierarchy:
        Советуется располагать в наследовании после абстрактного класса Drawable ради чёткого понимания и структурирования. 

    Methods:
        >>> update(self)

    Examples:
        >>> TrafficLight(Drawable, Updatable)
    """
    @abstractmethod
    def update(self):
        pass