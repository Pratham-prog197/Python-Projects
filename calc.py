print("Calculator")
print("\n")

num1 = float(input("Enter the first number here: "))
num2 = float(input("Enter the second number here: "))

print("Enter 1 for 'Addition' \nEnter 2 for 'Subtraction' \nEnter 3 for 'Multiply' \nEnter 4 for 'Divide'")

Entered_Number = int(input("Choose a number from 1 to 4: "))

if Entered_Number == 1:
    print("Addition of these numbers is:", num1 + num2)

elif Entered_Number == 2:
    print("Subtraction of these numbers is:", num1 - num2)

elif Entered_Number == 3:
    print("Multiplication of these numbers is:", num1 * num2)

elif Entered_Number == 4:
    if num2 != 0:
        print("Division of these numbers is:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")

else:
    print("Invalid input")
