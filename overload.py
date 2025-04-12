from typing import Union, overload

class Calculator:
    @overload
    def calculate(self, a: int, b: int) -> int:
        ...
 
    @overload
    def calculate(self, a: float, b: float) -> float:
        ...

    @overload
    def calculate(self, a: str, b: str) -> str:
        ...

    def calculate(self, a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(a, int) and isinstance(b, int):
            return a + b

        elif isinstance(a, float) and isinstance(b, float):
            return a + b

        elif isinstance(a, str) and isinstance(b, str):
            return a + b

        else:
            raise ValueError("Invalid input types")

result_handler: Calculator = Calculator()
output_1 = result_handler.calculate(2, 7)
output_2 = result_handler.calculate(2.3, 4.3)
output_3 = result_handler.calculate("saj", "eel")

print(output_1)
print(output_2)
print(output_3)
