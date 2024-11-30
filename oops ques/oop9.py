# Operator Overloading:
# Write python code to concatenate the two given strings
# using Operator Overloading





class StringConcatenator:
    def __init__(self, string1):
        self.string1 = string1

    def __add__(self, other):
        if isinstance(other, StringConcatenator):
            return self.string1 + other.string1
        elif isinstance(other, str):
            return self.string1 + other
        else:
            raise TypeError("Unsupported operand type(s) for +: 'StringConcatenator' and '{}'".format(type(other).__name__))

# Example usage
string1 = "Hello, "
string2 = "world!"
concatenator1 = StringConcatenator(string1)
concatenator2 = StringConcatenator(string2)

result = concatenator1 + concatenator2
print(result)
