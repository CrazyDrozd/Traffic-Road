"""Observer pattern implementation (Subject and Observer)."""

from typing import List
from abc import ABC, abstractmethod


# ==================== НАБЛЮДАТЕЛЬ ====================
class Observer(ABC):
    """
    Абстрактный класс паттерна наблюдателя. (наблюдатель)

    Реагирует на оповещения об изменениях в отслеживаемых субъектах.

    Methods:
        >>> update(self, *args, **kwargs)
    """
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


# ==================== СУБЪЕКТ ====================
class Subject(ABC):
    """
    Абстрактный класс паттерна наблюдателя. (субъект)

    Оповещает наблюдателей об изменениях в нём.

    Methods:
        >>> attach(self, observer: Observer)

        >>> detach(self, observer: Observer)

        >>> notify(self, *args, **kwargs)
    """
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        """
        Добавляет экземпляр класса в списки наблюдателей данного субъекта.
        
        Args:
            observer (Observer): Наблюдатель
        """
        if observer not in self._observers:
            if not isinstance(observer, Observer):
                raise TypeError(f"Expected Observer, got {type(listener).__name__}")
            
            self._observers.append(observer)
    
    def detach(self, observer: Observer):
        """
        Убирает экземпляр класса из списков наблюдателей данного субъекта.
        
        Args:
            observer (Observer): Наблюдатель
        """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, *args, **kwargs):  
        """
        Оповещает все экземпляры класса в списках наблюдателей данного субъекта.
        
        Args:
            *args
            **kwargs
        """
        for observer in self._observers:
            observer.update(*args, **kwargs)