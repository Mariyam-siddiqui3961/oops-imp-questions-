# Exception Handling:
# Write python code to create a class called “Calculator” with
# methods for addition, subtraction, multiplication, and
# division. Handle exceptions like division by zero gracefully
# and raise custom exceptions when needed.


class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        try:
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            return num1 / num2
        except ZeroDivisionError as e:
            print("Error:", e)
            return None
        except Exception as e:
            print("An error occurred:", e)
            return None

# Example usage
calculator = Calculator()

print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(5, 3))
print("Multiplication:", calculator.multiply(5, 3))
print("Division:", calculator.divide(5, 0))
print("Division:", calculator.divide(5, 2))
