# Class Methods and Static Methods:
# Create a class called “MathUtils” with class methods for
# calculating the factorial of a number and a static method to
# check if a number is even.

class MathUtils:
    @classmethod
    def factorial(cls, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Example usage
print("Factorial of 5:", MathUtils.factorial(5))
print("Is 6 even?", MathUtils.is_even(6))
