from operations import add, subtract, multiply, divide

def calculate(choice, a, b):
    if choice == 1:
        return add(a, b)
    elif choice == 2:
        return subtract(a, b)
    elif choice == 3:
        return multiply(a, b)
    elif choice == 4:
        return divide(a, b)
    else:
        return "Invalid choice"
if __name__ == "__main__":
    print(calculate(1, 2, 3))    