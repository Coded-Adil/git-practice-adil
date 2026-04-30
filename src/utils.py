## Create:

# add(a, b)
def add(a, b):
    return a + b

# subtract(a, b)
def subtract(a, b):
    return a - b

# multiply(a, b)
def multiply(a, b):
    return a * b

# divide(a, b)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# modulo(a, b)
def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero is not allowed."
    return a % b

# Call them main file.