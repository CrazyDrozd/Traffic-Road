"""Central event manager that dispatches Pygame events to registered listeners."""

import pygame

from typing import List

from data.interfaces.event_listeners import ClickListener, HoverListener, KeyListener

from logs.logging_system import init_logger

# ==================== МЕНЕДЖЕР СОБЫТИЙ ====================
class EventManager:
    """
    Основной менеджер событий. Отслеживает всевозможные события связанные с нажатием кнопок мыши, наведений мыши и нажатием клавиш.

    Methods:
        >>> register_click_listener(self, listener: ClickListener)

        >>> register_hover_listener(self, listener: HoverListener)

        >>> register_key_listener(self, listener: KeyListener)

        >>> handle_events(self)
    """
    def __init__(self):
        self.click_listeners: List[ClickListener] = []
        self.hover_listeners: List[HoverListener] = []
        self.key_listeners: List[KeyListener] = []

    def register_click_listener(self, listener: ClickListener):
        """
        Регистрирует наблюдателя за нажатием кнопок мыши.

        Args:
            listener: ClickListener
        """
        if not isinstance(listener, ClickListener):
            log.critical(f"Expected ClickListener, got {type(listener).__name__}")
            raise TypeError(f"Expected ClickListener, got {type(listener).__name__}")
            
        self.click_listeners.append(listener)

    def register_hover_listener(self, listener: HoverListener):
        """
        Регистрирует наблюдателя за наведением мыши.

        Args:
            listener: HoverListener
        """
        if not isinstance(listener, HoverListener):
            log.critical(f"Expected HoverListener, got {type(listener).__name__}")
            raise TypeError(f"Expected HoverListener, got {type(listener).__name__}")

        self.hover_listeners.append(listener)

    def register_key_listener(self, listener: KeyListener):
        """
        Регистрирует наблюдателя за нажатием клавиш.

        Args:
            listener: KeyListener
        """
        if not isinstance(listener, KeyListener):
            log.critical(f"Expected KeyListener, got {type(listener).__name__}")
            raise TypeError(f"Expected KeyListener, got {type(listener).__name__}")
        
        self.key_listeners.append(listener)

    def handle_events(self) -> bool:
        """
        Обрабатывает все события Pygame.
        Возвращает False, если получен сигнал QUIT, иначе True.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for listener in self.click_listeners:
                    listener.on_click(mouse_pos, event.button)

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for listener in self.hover_listeners:
                    listener.on_hover(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                for listener in self.key_listeners:
                    listener.on_key_down(event.key)

            elif event.type == pygame.KEYUP:
                for listener in self.key_listeners:
                    listener.on_key_up(event.key)

        return True
    

# ==================== ИНИЦИАЛИЗАЦИЯ ЛОГГЕРА ====================
log = init_logger(
        name = "eventmanager",  
        colored = True, 
        log_file = "logs/logs.log",
        level = "DEBUG"
    )
log.info('Logger of event_manager.py is initiated.')