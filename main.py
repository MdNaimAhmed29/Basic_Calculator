def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    result1=  x / y
    return f'{result1:.2f}'

def modulus(x, y):
       result2= x % y
       return f'{result2:.2f}'
def main():
    print("Select Operation:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Modulus")


    choice = input("Choice Operation (1/2/3/4/5): ")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "%", num2, "=", modulus(num1, num2))
        else:
            print("Invalid input")
    except Exception as error:
        print(error,'"Invalid input! Only Numeric Number"')

main()