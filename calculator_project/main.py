from calculator import calculate

print("Select an operation: ")
print("1. Addition") 
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Your choice: "))
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

results = calculate(choice, a, b)
print("Results:", results)
