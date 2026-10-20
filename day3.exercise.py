keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dictionary = dict(zip(keys, values))
print(my_dictionary)


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for key, value in family.items():

    if value < 3:
        ticket_price = 0
    elif value <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price
print(f"The total ticket cost is ${total_cost}")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = [0 if age < 3 else 10 if age <= 12 else 15 for age in family.values()]

print(dict(zip(family.keys(), price)))
print(f"The total ticket cost is ${sum(price)}")

family = {}

members = int(input("How many family members? "))

for i in range(members):
    name = input(f"Enter name of member {i + 1}: ")
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(f"{name} ({age}): ${price}")
    total_cost += price

print(f"The total ticket cost is ${total_cost}")





brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
clothes = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients are: {clothes}.")
brand["country_creation"] = "spain"
if "internation_competitors" in brand: 
    brand["international_competitors"].append("desigual")
del brand["country_creation"]
# Print the last item in international_competitors.
print(brand["international_competitors"][-1])
#Print the major colors in the US.
print(brand["major_color"]["US"])
#Print the number of keys in the dictionary.
print(len(brand))
#Print all keys of the dictionary.
print(brand.keys())



users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

result = {}

for index, name in enumerate(users):
    result[name] = index

print(result)

result[index] = name
print(result)   

result = {name: index for index, name in enumerate(sorted(users))}
    