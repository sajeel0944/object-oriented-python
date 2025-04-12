##   normal class
print("\nNormal class")

class Mom:
    def __init__(self, mom_name: str) -> None:
        self.mom_name: str = mom_name
        self.mom_eye_color: str = "blue"
    
    def speak(self, message: str) -> str:
        return f"Mother Speaking function: {message}"

class Dad:
    def __init__(self, dad_name: str) -> None:
        self.dad_name: str = dad_name
        self.dad_height: str = "6 Feet"

    def speak(self, message: str) -> str:
        return f"Father Speaking function: {message}"

class Kid(Mom, Dad):
    def __init__(self, mom_name: str, dad_name: str, kid_name: str) -> None:
        Mom.__init__(self, mom_name)
        Dad.__init__(self, dad_name)
        self.kid_name: str = kid_name

child1: Kid = Kid("Naseem Bano", "Muhammad Aslam", "Muhammad Qasim")

print(f"object height {child1.dad_height}")
print(f"object eye color {child1.mom_eye_color}")
print(child1.speak("Pakistan zinda bad"))
 




## dataclass

print("\nDataclass")

from dataclasses import dataclass, field

@dataclass
class Mom:
    mom_name: str
    mom_eye_color: str = "blue"

    def speak(self, message: str) -> str:
        return f"Mother Speaking function: {message}"

@dataclass
class Dad:
    dad_name: str
    dad_height: str = "6 Feet"

    def speak(self, message: str) -> str:
        return f"Father Speaking function: {message}"

@dataclass(init=False)
class Kid(Mom, Dad):
    kid_name: str

    def __init__(self, mom_name: str, dad_name: str, kid_name: str):
        Mom.__init__(self, mom_name)
        Dad.__init__(self, dad_name)
        self.kid_name = kid_name

child1: Kid = Kid("Naseem Bano", "Muhammad Aslam", "Muhammad Qasim")

print(f"object height: {child1.dad_height}")
print(f"object eye color: {child1.mom_eye_color}")
print(child1.speak("Pakistan zinda bad"))
