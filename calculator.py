def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def root(x, y):
    return x ** (1 / y)
  
def Menu():
  
    print("Select operation.")

    print("1.Add")

    print("2.Subtract")

    print("3.Multiply")

    print("4.Divide")

    print("5.Power")

    print("6.Root")
  
    return None

def Calculator():
    while True:
        Menu()
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
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
                    if num2 == 0:
                        print("AI: You cannot divide by zero.")
                        continue
                    print(num1, "/", num2, "=", divide(num1, num2))

                elif choice == '5':
                    print(num1, "**", num2, "=", power(num1, num2))

                elif choice == '6':
                    if num2 == 0:
                        print("AI: The root number cannot be zero.")
                        continue
                    print(num1, "√", num2, "=", round(root(num1, num2), 2))

            except ValueError:
                print("AI: Please enter a valid number.")
                continue

            except ZeroDivisionError:
                print("AI: You cannot divide by zero.")
                continue

            next_calculation = input("Let's do another calculation? (yes/no): ")

            if next_calculation.lower() != "yes":
                break

        else:
            print("AI: Invalid choice.")
