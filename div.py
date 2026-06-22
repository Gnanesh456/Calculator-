a=float(input("Enter numerator :"))

b=float(input("Enter denominator :"))

def divide(a,b):
    if b==0:
        print("Error: Division by zero is not possible.")
    else:
        return a/b
print("The result of Division is :",divide(a,b))