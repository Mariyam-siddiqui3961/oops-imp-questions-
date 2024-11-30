# Lamda functions:
# Write python code to perform the following Lamda function
# below:
# (i) Map()
# (ii) filter()
# (iii) lambda function to calculate grades for a list of scores.
# (iv) List Comprehensions.
# (v) calculates the factorial of a number using a recursive
# lambda function


# (i) Map:

# python
# Copy code
# Example of map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]



# (ii) Filter:

# python
# Copy code
# Example of filter function
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]



# (iii) Lambda function to calculate grades for a list of scores:

# python
# Copy code
# Example of lambda function to calculate grades
scores = [85, 90, 60, 75, 95]
grades = list(map(lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F', scores))
print(grades)  # Output: ['B', 'A', 'D', 'C', 'A']

# (iv) List Comprehensions:

# python
# Copy code
# Example of list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# (v) Recursive lambda function to calculate factorial:

# python
# Copy code
# Example of recursive lambda function to calculate factorial
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))  # Output: 120