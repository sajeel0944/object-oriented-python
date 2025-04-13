# normal class
class GreetUser:
    def __init__(self, user_name):
        self.user_name = user_name

    def __str__(self):
        return f"Hello {self.user_name}"

user_instance: GreetUser = GreetUser("sajeel")
print(user_instance)


# dataclass
from dataclasses import dataclass

@dataclass
class GreetUser:
    user_name: str

    def __str__(self):
        return f"Hello {self.user_name}"

user_instance: GreetUser = GreetUser("sajeel")
print(user_instance)
