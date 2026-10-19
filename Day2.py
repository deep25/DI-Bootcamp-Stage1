my_fav_numbers = [7, 14, 21, 28, 35]
my_fav_numbers.append(42)
print(my_fav_numbers)
my_fav_numbers.remove(42)
friend_fav_numbers = [3, 6, 9, 12, 15]
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)


# float is a number with a decimal point, while an integer is a whole number without a decimal point. For example, 3.14 is a float, while 3 is an integer.
numbers = []

for i in range(1, 5):
    numbers.append(i + 0.5)   # float: 1.5, 2.5, 3.5, 4.5
    numbers.append(i + 1)     # int:   2, 3, 4, 5

print(numbers)

a = range(1, 21)
for num in a:
    if num % 2 == 0:
        print(num)

while True:
    name = input("Enter your name: ")

    if name.isdigit() or len(name) < 3:
        print("That is not a proper name. Please try again.")
    else:
        print("Thank you")
        break


fav_fruit = input("Enter your favorite fruit: ")
list_of_favfruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
if fav_fruit in list_of_favfruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")



Topping = input("Enter a pizza topping: ")
avl_toppings = {"pepperoni": 3.0, "mushrooms": 2.5, "onions": 2.0, "sausage": 3.5, "bacon": 4.0}
Pizza_price = 10.0
for Topping in avl_toppings:
    total_price = Pizza_price + avl_toppings[Topping]
    print(f"The total price for a pizza with {Topping} is ${total_price:.2f}")




people = int(input("How many people are in the family? "))
total = 0

for person in range(1, people + 1):
    age = int(input(f"Enter the age of person {person}: "))

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total = total + price

print(f"The total ticket cost is ${total}")
    