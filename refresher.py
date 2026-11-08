from typing import Any
import json
import dataclasses


def average(numbers: list[int]) -> float:
    if not numbers:
        return 0.0

    total = sum(numbers)
    count = len(numbers)
    return total / count


calculus = average([59033, 8, 1551, 988, 17])
print(calculus)
# Project A done. lets go to project B


@dataclasses.dataclass
class Expense:
    name: str
    category: str
    amount: float


Ahmad = Expense(name="Ahmad", category="Food", amount=15.50)
print(Ahmad.amount)
# Now lets dive into task C & D


def load_json(path: str) -> Any:
    try:
        with open(path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return []
# Now task E :


def total_amount(expenses: list[Expense]) -> float:
    total = 0.0
    for expense in expenses:
        total += expense.amount
    return total


if __name__ == "__main__":
    # Create a couple of fake expenses using our Expense class
    item1 = Expense(name="Groceries", category="Food", amount=45.50)
    item2 = Expense(name="Gas", category="Transport", amount=30.00)

    # Put them in a list
    my_shopping_list = [item1, item2]

    # Call our total_amount function and print the result
    result = total_amount(my_shopping_list)
    print(f"Total expense amount: ${result}")  # Should print: 75.5
