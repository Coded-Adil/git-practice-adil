from utils import add, subtract, multiply, divide

## Write a simple program:

## Print your name
print("Name: Adil Rahman")

## Print today’s date
print("Date: 30-04-2026")

## calling functions from utils.py
add_result = add(5, 3)
subtract_result = subtract(10, 4)
multiply_result = multiply(6, 7)
safe_division_result = divide(20, 5)
unsafe_division_result = divide(10, 0)

print(f"Addition Result: {add_result}")
print(f"Subtraction Result: {subtract_result}")
print(f"Multiplication Result: {multiply_result}")
print(f"Safe Division Result: {safe_division_result}")
print(f"Unsafe Division Result: {unsafe_division_result}")