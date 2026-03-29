"""Logging system."""

import logging
import logging.handlers

from time import sleep
from typing import Optional

# ==================== КЛАСС ФОРМАТА ЛОГОВ ====================
class CustomFormatter(logging.Formatter):
	grey = "\x1b[38;20m"
	yellow = "\x1b[33;20m"
	red = "\x1b[31;20m"
	bold_red = "\x1b[31;1m"
	reset = "\x1b[0m"
	base_format = "(%(filename)s:%(lineno)d) [%(asctime)s]    %(levelname)s %(name)s: %(message)s"

	def __init__(self, colored: Optional[bool] = True):
		super().__init__()
		self.colored = colored
		self.FORMATS = {
			logging.DEBUG: self.grey + self.base_format + self.reset,
			logging.INFO: self.grey + self.base_format + self.reset,
			logging.WARNING: self.yellow + self.base_format + self.reset,
			logging.ERROR: self.red + self.base_format + self.reset,
			logging.CRITICAL: self.bold_red + self.base_format + self.reset
		}

	def format(self, record):
		if self.colored:
			log_format = self.FORMATS.get(record.levelno, self.base_format)
		else:
			log_format = self.base_format
		formatter = logging.Formatter(log_format)
		return formatter.format(record)


# ==================== ИНИЦИАЛИЗАТОР ЛОГОВ ====================
def init_logger(name: str, colored: bool, log_file: Optional[str] = None, level: str = "DEBUG"):
	"""
    Инициализирует и настраивает логгер.

    Создаёт логгер с указанным именем, настраивает вывод в консоль
    и опционально в файл.

    Args:
        name (str): Имя логгера (обычно __name__)
        coloreed (bool): Будут ли логи в консоли быть различных цветов в зависимости от уровня логирования
        log_file (Optional[str]): Путь к файлу для записи логов.
                                  Если None, логи выводятся только в консоль.
        level (str): Уровень логирования ("DEBUG", "INFO", "WARNING", "ERROR")

    Returns:
        logging.Logger: Настроенный экземпляр логгера

    Raises:
        ValueError: Если указан неподдерживаемый уровень логирования
        OSError: Если не удаётся создать или открыть файл для записи

    Example:
        >>> logger = init_logger("logger", True, "logs.log", "DEBUG")
        >>> logger.info("Логгер инициализирован")
    """
	log = logging.getLogger(name)

	if log.handlers:
		return log

	log.setLevel(level)

	ConsoleHandler = logging.StreamHandler()
	ConsoleHandler.setLevel(level)
	ConsoleHandler.setFormatter(CustomFormatter(colored=colored))
	log.addHandler(ConsoleHandler)

	if log_file is not None:
		FileHandler = logging.handlers.RotatingFileHandler(log_file)
		FileHandler.setLevel(logging.INFO)
		FileHandler.setFormatter(logging.Formatter("(%(filename)s:%(lineno)d) [%(asctime)s]    %(levelname)s %(name)s: %(message)s"))
		log.addHandler(FileHandler)

	return log


# ==================== ЗАПУСК ФАЙЛА + ТЕСТ ЛОГОВ ====================
if __name__ == "__main__":
	log = init_logger(name = "Test", colored = True, log_file = "Test.log", level = "DEBUG")

	log.debug("debug message")
	log.info("info message")
	log.warning("warning message")
	log.error("error message")
	log.critical("critical message")

	while True:
		sleep(1)