cont = True
while cont==True:
    try:
        number = int(input("Please enter a number between 1-100: "))
        if number <= 100 and number >= 1:
            print(number)
            cont = False
        elif number > 100:
            print("That number is too large")
        elif number < 1:
            print("That number is too small")
    except ValueError:
        print("That is not an interger")
