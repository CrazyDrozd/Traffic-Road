"""Game configuration dataclass."""

from dataclasses import dataclass
from typing import Tuple


# ==================== CONFIGURATION ====================
@dataclass
class GameConfig:
    DEBUG: bool = True
    CAPTION: str = "Traffic Road"
    VERSION: str = 'Prototype [18-03-2026]'
    WINDOW_WIDTH: int = 1280
    WINDOW_HEIGHT: int = 720
    FPS: int = 60
    BACKGROUND_COLOR: Tuple[int, int, int] = (240, 234, 214)