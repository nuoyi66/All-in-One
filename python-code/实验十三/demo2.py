while True:
    try:
        x = int(input("Please enter a integer"))
        print("x=%d"%x)
        break
    except ValueError:
        print("That was no Valid number.Try again")