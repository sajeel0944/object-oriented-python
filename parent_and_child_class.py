##   normal class
print("\nNormal class")
 
class Employee:
    def __init__(self, emp_name: str, emp_qualification: str, emp_department: str) -> None:
        self.emp_name: str = emp_name
        self.emp_qualification: str = emp_qualification
        self.emp_department: str = emp_department

    def display(self) -> str:
        return f"Name: {self.emp_name}, Department: {self.emp_department}, Qualification: {self.emp_qualification}"


class Designer(Employee):
    def __init__(self, emp_name: str, emp_qualification: str) -> None:
        super().__init__(emp_name, emp_qualification, "Designer")


class Developer(Employee):
    def __init__(self, emp_name: str, emp_qualification: str) -> None:
        super().__init__(emp_name, emp_qualification, "Developer")


designer_1: Designer = Designer("sajeel", "Graphics Design")
developer_1: Developer = Developer("saif", "AI Assistant")

print(designer_1.display())
print(developer_1.display())




# dataclass
print("\nDataclass")

from dataclasses import dataclass

@dataclass
class Employee:
    emp_name: str
    emp_qualification: str
    emp_department: str

    def display(self) -> str:
        return f"Name: {self.emp_name}, Department: {self.emp_department}, Qualification: {self.emp_qualification}"


@dataclass
class Designer(Employee):
    emp_name: str
    emp_qualification: str
    emp_department: str = "Designer"


@dataclass
class Developer(Employee):
    emp_name: str
    emp_qualification: str
    emp_department: str = "Developer"


designer_1: Designer = Designer("sajeel", "Graphics Design")
developer_1: Developer = Developer("saif", "AI Assistant")

print(designer_1.display())
print(developer_1.display())

