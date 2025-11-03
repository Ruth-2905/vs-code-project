def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

if __name__ == "__main__":
    first_number =input("Enter your first_number ")
    second_number =input("Enter your second_number ")
    operator =input("Enter the operator (+, _, /, *) ")

    first_number = int(first_number)
    second_number = int(second_number)

    if operator == "+":
        result = sum(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "/":
        result = divide(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    
    print(f"{first_number} {operator} {second_number} = {result} ")

