from typing import Iterator, Optional
from engine.comps import Actor


class Engine(object):
    """The core of the roguelike game."""

    def __init__(self, scheduler: Iterator[Actor]) -> None:
        self.scheduler: Iterator[Actor] = scheduler

    def tick(self) -> None:
        pass
