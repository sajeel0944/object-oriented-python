#                   using ( __ )

# normal class

print("\nNormal class")

class Valify_user:
    def __init__(self) -> None:
        self.__user_email : list[str] = []
        self.__user_password : list[str] = []

    def __connectivity(self, email: str, password: str) -> str:

        find_user_email = list(filter(lambda value : value == email, self.__user_email))
        find_user_password = list(filter(lambda value : value == password, self.__user_password))

        if find_user_email and find_user_password:
            return "valid user"
        else:
            return "invaild user"
         

    def sign_in(self, email: str, password: str) -> None:
        self.__user_email.append(email)
        self.__user_password.append(password)

    
    def login(self, email: str, password: str) -> str:
        check_data = self.__connectivity(email, password)
        return check_data


user : Valify_user = Valify_user()
singin = user.sign_in("sajeel", "4490")
login = user.login("sajeel", "4490")
print(login)

login = user.login("saif", "4490")
print(login)




# dataclass

print("\nDataclass")

from dataclasses import dataclass, field

@dataclass
class Valify_user:
    __user_email : list[str] = field(default_factory=list)
    __user_password : list[str] = field(default_factory=list)

    def __connectivity(self, email: str, password: str) -> str:

        find_user_email = list(filter(lambda value : value == email, self.__user_email))
        find_user_password = list(filter(lambda value : value == password, self.__user_password))

        if find_user_email and find_user_password:
            return "valid user"
        else:
            return "invaild user"
        

    def sign_in(self, email: str, password: str) -> None:
        self.__user_email.append(email)
        self.__user_password.append(password)

    
    def login(self, email: str, password: str) -> str:
        check_data = self.__connectivity(email, password)
        return check_data


user : Valify_user = Valify_user()
singin = user.sign_in("sajeel", "4490")
login = user.login("sajeel", "4490")
print(login)

login = user.login("saif", "4490")
print(login)


