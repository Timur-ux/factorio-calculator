from abc import ABCMeta, abstractmethod
from collections.abc import Iterator

class BaseItem(metaclass=ABCMeta):
    @abstractmethod
    def name(self) -> str:
        """Returns Item's name"""
        ...
    
    @abstractmethod
    def components(self) -> dict:
        """Returns Item's compounents"""
        ...

    @abstractmethod
    def creationTime(self) -> float:
        """Returns Item's creation time"""
        ...
    
    @abstractmethod
    def __iter__(self) -> Iterator:
        """Iterates through compounents"""
        ...

class Item(BaseItem):
    def __init__(self, name: str,  creationTime: float, components: dict[BaseItem, int] = {}):
        self.name_ = name
        self.components_ = components
        self.creationTime_ = creationTime
    
    def name(self):
        return self.name_

    def components(self):
        return self.components_

    def creationTime(self):
        return self.creationTime_

    def __iter__(self):
        return iter(self.components())
