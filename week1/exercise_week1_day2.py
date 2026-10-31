my_fav_numbers = {2, 4, 5, 8, 9, 10}
add_num = my_fav_numbers.update([11,12])
print(my_fav_numbers)

remove_num = my_fav_numbers.remove(12)
print(my_fav_numbers)

friend_fav_numbers = {3, 1, 7, 6}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
remove_basket = basket.remove('Banana')
print(basket)

remove_basket = basket.remove('Blueberries')

add_fruit = basket.append('Kiwi')

add_f = basket.append('Apples')

count_f = basket.count('Apples')

clear_list = basket.clear()
print(basket)


#A float is a number with a decimal point, like 1.5, 3.14 or -0.25.
#An integer (int) is a whole number with no decimal point, like 2, 100 or -7.
#The difference is whether the number has a decimal part. Python treats 2 (an integer) and 2.0 (a float) as different types, even though they have the same value

numbers = []

for i in range(1,5):
    numbers.append(i + .5)
    numbers.append(i + 1)
print(numbers)


list_num =[]

for i in range(1,21):
    if i % 2 == 0:
     print(i)


a = range(1, 21)
for num in a:
    if num % 2 == 0:
        print(num)


while True:
   user_input = input("Enter your name.")
   if user_input.isdigit() or len(user_input) < 3:
      print("Give a correct name")

   else:
      print("Thank you")
      break

user_inputs = input("Enter your favourite fruits: ").split()
fruits = [user_inputs]

user_asks = input("Enter a fruit: ")
if user_asks in user_inputs:
   print("your favourite fruit")
else:
   print("You chose a new fruit. I hope you enjoy it!")


toppings = []

base_prize_pizza = 10
each_topping = 2.5

while True:

    user_inputs_topping = input("Enter your pizza toppings: ")

    if user_inputs_topping == 'quit':
       break
    print(f"adding {user_inputs_topping} to your pizza")

    toppings.append(user_inputs_topping)
    total_topping = (len(toppings) * each_topping)

for total in user_inputs_topping:
   total = total_topping + base_prize_pizza
print(f"Your total amount is : {total}")



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
     






