#  normal class
print("\nNormal class")
 
class UserInfo:
    def __init__(self, user_name: str, user_password: int, user_email: str) -> None:
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email

    def manage(self) -> str:
        return f"user information : {self.user_name}, {self.user_password}, {self.user_email}"

    def check(self) -> str:
        if self.user_name == "sajeel" and self.user_email == "saj@gmail.com" and self.user_password == 333:
            return "Welcome To Sajeel"
        else:
            return "Wrong Password"


save: UserInfo = UserInfo("sajeel", 333, "saj@gmail.com")
display = save.manage()
display_1 = save.check()
print(display)
print(display_1)




# dataclass

print("\nDataclass")

from dataclasses import dataclass

@dataclass
class UserInfo:
    user_name: str
    user_password: int
    user_email: str

    def manage(self) -> str:
        return f"user information : {self.user_name}, {self.user_password}, {self.user_email}"

    def check(self) -> str:
        if self.user_name == "sajeel" and self.user_email == "saj@gmail.com" and self.user_password == 333:
            return "Welcome To Sajeel"
        else:
            return "Wrong Password"

 
save: UserInfo = UserInfo("sajeel", 333, "saj@gmail.com")
display = save.manage()
display_1 = save.check()
print(display)
print(display_1)





