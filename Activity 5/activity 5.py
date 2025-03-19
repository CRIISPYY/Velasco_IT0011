def main():
    while True:
        print("============================================")
        print("\t\tMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        print("============================================")
        print("Note: Please use capital letters")
        
        choice = input("Enter your choice: ")
        
        if choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        elif choice in ['D', 'E', 'R', 'F']:
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue
            
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiate(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                result = summation(num1, num2)

            if result is not None:
                print(f"\nResult: {result}")
        else:
            print("\nInvalid choice. Please type a choice of letter in capital letter")

def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return None
    return num1 / num2

def exponentiate(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return num1 % num2

def summation(num1, num2):
    if num1 > num2:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(num1, num2 + 1))

def get_numbers():
    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid integers.")
        return None, None

if __name__ == "__main__":
    main()
