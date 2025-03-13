from abc import ABC, abstractmethod

class Animal(ABC):
    """Must iclude the properties ( name, food_type )"""

    # @property
    # @abstractmethod
    # def name(self):
    #     pass  # Abstract property, must be implemented by subclasses

    # @property
    # @abstractmethod
    # def food_type(self):
    #     pass  # Abstract property, must be implemented by subclasses

    def __feed__(self, daily_feedings: int = 3) -> str:
        return(f"{self.name} must be fed {self.food_type} .")