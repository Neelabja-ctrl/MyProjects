import math

def show_menu():
    print("\n" + "="*30)
    print("     SCIENTIFIC CALCULATOR     ")
    print("="*30)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power ($x^y$)")
    print("6. Square Root ($\sqrt{x}$)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Natural Logarithm (ln)")
    print("11. Base-10 Logarithm (log10)")
    print("0. Exit")
    print("="*30)

def calculator():
    while True:
        show_menu()
        choice = input("Enter choice (0-10): ").strip()

        if choice == '0':
            print("Goodbye!")
            break

        # Basic Arithmetic (Requires two inputs)
        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {math.pow(num1, num2)}")

        # Scientific Functions (Requires one input)
        elif choice in ['6', '7', '8', '9', '10', '11']:
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
                continue

            if choice == '6':
                if num < 0:
                    print("Error: Cannot take the square root of a negative number.")
                else:
                    print(f"Result: √{num} = {math.sqrt(num)}")

            elif choice in ['7', '8', '9']:
                # math functions expect radians, so we convert degrees to radians first
                rad = math.radians(num)
                if choice == '7':
                    print(f"Result: sin({num}°) = {math.sin(rad)}")
                elif choice == '8':
                    print(f"Result: cos({num}°) = {math.cos(rad)}")
                elif choice == '9':
                    # Checking for undefined tangent values (e.g., 90, 270 degrees)
                    if (num - 90) % 180 == 0:
                        print(f"Result: tan({num}°) is Undefined")
                    else:
                        print(f"Result: tan({num}°) = {math.tan(rad)}")

            elif choice == '10':
                if num <= 0:
                    print("Error: Logarithm undefined for values ≤ 0.")
                else:
                    print(f"Result: ln({num}) = {math.log(num)}")

            elif choice == '11':
                if num <= 0:
                    print("Error: Logarithm undefined for values ≤ 0.")
                else:
                    print(f"Result: log10({num}) = {math.log10(num)}")

        else:
            print("Invalid choice! Please select a valid option from the menu.")

# Run the calculator
if __name__ == "__main__":
    calculator()