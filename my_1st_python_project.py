while True:
    try:
        num = int(input("Enter a Number: "))
        if num % 2 == 0:
            print("The Number", num, "is even.")
        else:
            print("The Number", num, "is odd.")

        decision = input("\nDo you want to continue playing? Yes(Y) / No(N): ").lower()
        if decision not in ['yes', 'y']:
            print("Thank you for playing!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
