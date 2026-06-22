def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = divide_numbers(num1, num2)
print("Result:", result)