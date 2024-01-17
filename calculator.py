def simple_math():
    print("Welcome to the simple calculator !")
    first_num = float(input("Provide the first number: "))
    second_num = float(input("Provide the second number: "))
    print("Choose an operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = input("Make a selection(1/2/3/4): ")

    if operation == '1':
        outcome = first_num + second_num
        print("The outcome is: ", outcome)
    elif operation == '2':
        outcome = first_num - second_num
        print("The outcome is: ", outcome)
    elif operation == '3':
        outcome = first_num * second_num
        print("The outcome is: ", outcome)
    elif operation == '4':
        if second_num != 0:
            outcome = first_num / second_num
            print("The outcome is: ", outcome)
        else:
            print("Error! Cannot divide by zero.")
    else:
        print("Invalid selection Try again")

simple_math()
