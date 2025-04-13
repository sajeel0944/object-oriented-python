# normal class 

from abc import ABC, abstractmethod
from typing import Union

class Creature(ABC):
    @abstractmethod
    def __init__(self, creature_name: str, creature_age: int):
        self.creature_name: str = creature_name
        self.creature_age: int = creature_age

    @abstractmethod
    def display_info(self) -> str:
        pass

class Cat(Creature):
    def __init__(self, creature_name: str, creature_age: int):
        super().__init__(creature_name, creature_age)

    def display_info(self) -> Union[str, int]:
        return f"Name : {self.creature_name} and age : {self.creature_age}"

cat_instance: Cat = Cat("Sajeel", 19)
print(cat_instance.display_info())




# dataclass

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union

@dataclass
class Creature(ABC):
    creature_name: str
    creature_age: int

    @abstractmethod
    def display_info(self) -> str:
        pass

@dataclass
class Cat(Creature):
    def display_info(self) -> Union[str, int]:
        return f"Name : {self.creature_name} and age : {self.creature_age}"

cat_obj: Cat = Cat("Sajeel", 19)
print(cat_obj.display_info())
