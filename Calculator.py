a=float(input("Enter the first value:-"))
b=float(input("Enter the second value:-"))
print("Choose the operator:-\n"
      "1.Additon\n"
      "2.Subtraction\n"
      "3.Multiplicatin\n"
      "4.Division\n"
      "5.Modulo\n"
      "6.Exponentiation\n")
choice=int(input("Enter your choice to perform the opration:-"))
print("You choose:",choice)
if choice == 1:
    print("Addition of two number is:",a+b)
elif choice == 2:
    print("Subtraction of two number is:",a-b)
elif choice == 3:
    print("Multiplication is:",a*b)
elif choice == 4: 
    try:
        print("Te modular is:",a/b)
    except ZeroDivisionError:
        print("Value cannot divided by zero")
elif choice== 5:
        print("Te modular is:",a%b)
elif choice == 6:
    print("The exponentiation is:",a**b)
else:
    print("Invalid choice")
print("Operation performed succesfully!")