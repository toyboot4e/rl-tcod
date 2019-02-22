import tcod
from abc import ABCMeta, abstractmethod


class Scene(metaclass=ABCMeta):
    @abstractmethod
    def handle_imput(self, key: tcod.Key, mouse: tcod.Mouse) -> None: pass
    @abstractmethod
    def render(self) -> None: pass
