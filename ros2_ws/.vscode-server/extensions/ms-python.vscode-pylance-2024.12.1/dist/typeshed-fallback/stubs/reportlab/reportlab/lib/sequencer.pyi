from _typeshed import Incomplete

__all__ = ["Sequencer", "getSequencer", "setSequencer"]

class _Counter:
    def __init__(self) -> None: ...
    def setFormatter(self, formatFunc) -> None: ...
    def reset(self, value: Incomplete | None = None) -> None: ...
    def next(self): ...
    __next__ = next
    def nextf(self): ...
    def thisf(self): ...
    def chain(self, otherCounter) -> None: ...

class Sequencer:
    def __init__(self) -> None: ...
    def __next__(self): ...
    def next(self, counter: Incomplete | None = None): ...
    def thisf(self, counter: Incomplete | None = None): ...
    def nextf(self, counter: Incomplete | None = None): ...
    def setDefaultCounter(self, default: Incomplete | None = None) -> None: ...
    def registerFormat(self, format, func) -> None: ...
    def setFormat(self, counter, format) -> None: ...
    def reset(self, counter: Incomplete | None = None, base: int = 0) -> None: ...
    def chain(self, parent, child) -> None: ...
    def __getitem__(self, key): ...
    def format(self, template): ...
    def dump(self) -> None: ...

def getSequencer(): ...
def setSequencer(seq): ...