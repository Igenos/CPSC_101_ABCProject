from abc import ABC, abstractmethod

class Animal(ABC):
    """Must iclude the properties (name, food_type)"""

    # @property
    # @abstractmethod
    # def name(self) -> str:
    #     pass

    # @property
    # @abstractmethod
    # def food_type(self) -> str:
    #     pass  # Abstract property, must be implemented by subclasses. In this case we want it to be overwritten, so we do not use __food_type__

    # The double underscores around feed is an example on "name mangling", what that means is that this method cannot be overwritten by the child class.
    def __feed__(self, daily_feedings: int = 3) -> str:
        return(f"{self.name} must be fed {self.food_type} .")
    
    @abstractmethod
    def eat(self: object) -> str:
        pass