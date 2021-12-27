from abc import ABC, abstractmethod
from __future__ import annotations


class Entity(ABC): 
    health: int
    max_health: int
    frozen: bool

    @abstractmethod
    def decrease_health(self, value: int) -> None:
        pass

    @abstractmethod
    def freeze(self) -> None:
        pass
    
    @abstractmethod
    def unfreeze(self) -> None:
        pass

