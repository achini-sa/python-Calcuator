# Calculator

def Addition(x, y):
    return x + y

def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y

def Exponentiation(x, y):
    return x ** y

def Division(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def Floor_division(x, y):
    if y != 0:
        return x // y
    else:
        return "Cannot divide by zero"
    
def Modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Cannot divide by zero"
    
    
def calculator(num1, operator, num2):
    if operator == '+':
        return Addition(num1, num2)
    elif operator == '-':
        return Subtraction(num1, num2)
    elif operator == '*':
        return Multiplication(num1, num2)
    elif operator == '**':
        return Exponentiation(num1, num2)
    elif operator == '/':
        return Division(num1, num2)
    elif operator == '//':
        return Floor_division(num1, num2)
    elif operator == '%':
        return Modulus(num1, num2)
    
    else:
        return "Invalid operator"
    

# Example usage:
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, **, /, //, % ): ")
num2 = float(input("Enter second number: "))

result = calculator(num1, operator, num2)
print("Result:", result)

# Run the application
