if user.lower() == "calculate":
    while True:
        Menu()
        choice = input("Enter choice(1/2/3/4/5/6): ")

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
                    print(num1, "/", num2, "=", divide(num1, num2))

                elif choice == '5':
                    print(num1, "**", num2, "=", power(num1, num2))

                elif choice == '6':
                    print(num1, "√", num2, "=", round(root(num1, num2), 2))

            except:
                print("AI: Please enter a valid number.")
              
            next_calculation = input("Let's do next calculation? (yes/no): ")

            if next_calculation.lower() != "yes":
                break

        else:
            print("Invalid Input")

    continue
