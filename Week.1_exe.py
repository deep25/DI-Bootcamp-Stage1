print("Hello world\n" * 4 + "I love python\n" * 3 + "I love python")



month = input("Enter a month: ").strip().capitalize()

if month in ("March", "April", "May"):
    print("It's spring.")
elif month in ("June", "July", "August"):
    print("It's summer.")
elif month in ("September", "October", "November"):
    print("It's fall.")
elif month in ("December", "January", "February"):
    print("It's winter.")
else:
    print("That is not a month I know.")

    