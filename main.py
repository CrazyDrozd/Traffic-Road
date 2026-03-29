"""Project Core"""

import pygame
import sys

from typing import List

from data.config import GameConfig
from data.event_manager import EventManager
from data.interfaces.sprite_interfaces import Drawable, Updatable

from data.ui.button import Button
from data.ui.debug import DebugButton, DebugOverlay

from logs.logging_system import init_logger

# ==================== ОСНОВНОЙ ИНИЦИАЛИЗАТОР ИГРЫ ====================
class Game:
    def __init__(self, config: GameConfig = None):
        pygame.init()
        self.config = config or GameConfig()
        self.screen = pygame.display.set_mode(
            (self.config.WINDOW_WIDTH, self.config.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(self.config.CAPTION)

        self.clock = pygame.time.Clock()
        self.running = True

        self.event_manager = EventManager()

        self._init_components()
        self._register_listeners()
        self._draw_drawables()

    def _init_components(self):
        self.debug_button = DebugButton(10, 10, self.config)
        self.debug_overlay = DebugOverlay(self.config, self.debug_button, offset_x=5, offset_y=40)

        self.buttons: List[Button] = [
            self.debug_button
        ]

        self.drawables: List[Drawable] = [
            self.debug_button,
            self.debug_overlay
        ]

    def _register_listeners(self):
        self.event_manager.register_key_listener(self.debug_overlay)

        for button in self.buttons:
            self.event_manager.register_click_listener(button)
            self.event_manager.register_hover_listener(button)

        log.debug(f'''Objects were registered in event manager as following listeners: 
            ╰┈    Click: {self.event_manager.click_listeners}
            ╰┈    Hover: {self.event_manager.hover_listeners}
            ╰┈    Key: {self.event_manager.key_listeners}''')

    def _update_drawables(self):
        for obj in self.drawables:
                if isinstance(obj, Updatable):
                    obj.update()

    def _draw_drawables(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)

        for drawable in self.drawables:
            drawable.draw(self.screen)

        pygame.display.flip()

    def run(self):
        log.info('Game is running.')
        while self.running:
            if not self.event_manager.handle_events():
                self.running = False  # pygame.QUIT

            self._update_drawables()
            self._draw_drawables()
            self.clock.tick(self.config.FPS)

        pygame.quit()
        sys.exit()


# ==================== ЗАПУСК ИСХОДНИКА ====================
if __name__ == "__main__":
    log = init_logger(
        name = "TrafficRoad",  
        colored = True, 
        log_file = "logs/logs.log",
        level = "DEBUG"
    )
    log.info('Initiated logging system.')

    game = Game()
    game.run()