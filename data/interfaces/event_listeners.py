"""Event Listeners: ClickListener, HoverListener, KeyListener."""

from abc import ABC, abstractmethod
from typing import Tuple


# ==================== СЛУШАТЕЛЬ НАЖАТИЙ МЫШИ ====================
class ClickListener(ABC):
    """
    Абстрактный класс, обозначающий, что последующие классы, наследующие основной метод:
        —— Способны реагировать на нажатия кнопки мыши.

    Один из трёх интерфейсов событий:
        >>> ClickListener(Abc)

        >>> HoverListener(ABC)

        >>> KeyListener(ABC)

    Hierarchy:
        Советуется распологать в наследовании после абстрактных классов спрайтов в последовательности, указанной выше.

    Methods: 
        >>> on_click(self, mouse_pos: Tuple[int, int], button: int)
    
    Examples:
        >>> Button(Drawable, ClickListener, HoverListener, ABC)
    """
    @abstractmethod
    def on_click(self, mouse_pos: Tuple[int, int], button: int):
        pass


# ==================== СЛУШАТЕЛЬ НАВЕДЕНИЙ ====================
class HoverListener(ABC):
    """
    Абстрактный класс, обозначающий, что последующие классы, наследующие основной метод:
        —— Способны реагировать на наведения мыши.

    Один из трёх интерфейсов событий:
        >>> ClickListener(Abc)

        >>> HoverListener(ABC)

        >>> KeyListener(ABC)

    Hierarchy:
        Советуется распологать в наследовании после абстрактных классов спрайтов в последовательности, указанной выше.

    Methods: 
        >>> on_hover(self, mouse_pos: Tuple[int, int])
    
    Examples:
        >>> Button(Drawable, ClickListener, HoverListener, ABC)
    """
    @abstractmethod
    def on_hover(self, mouse_pos: Tuple[int, int]):
        pass


# ==================== СЛУШАТЕЛЬ НАЖАТИЙ КЛАВИШ ====================
class KeyListener(ABC):
    """
    Абстрактный класс, обозначающий, что последующие классы, наследующие основной метод:
        —— Способны реагировать на нажатия клавиш.

    Один из трёх интерфейсов событий:
        >>> ClickListener(Abc)

        >>> HoverListener(ABC)

        >>> KeyListener(ABC)

    Hierarchy:
        Советуется распологать в наследовании после абстрактных классов спрайтов в последовательности, указанной выше.

    Methods: 
        >>> on_key_down(self, key: int)

        >>> on_key_up(self, key: int)
    
    Examples:
        >>> DebugOverlay(Drawable, KeyListener)
    """
    @abstractmethod
    def on_key_down(self, key: int):
        pass

    @abstractmethod
    def on_key_up(self, key: int):
        pass