"""Use arrays to simulate grade-school multiplication."""


def multiply(num1, num2):
    """Input two arrays of integers and muliply both as if two numbers."""
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1

