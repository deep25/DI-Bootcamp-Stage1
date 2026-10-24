
def display_message(message):
    return message

message = display_message("I am learning about function in python")
print(message)


def favourite_book(title):
    return title
call = favourite_book("Alice in wonderland")
print(f"one of my favourite book is {call}")


def describe_city(city, country= "Unknown"):
    return city, country

geo = describe_city(city= "Reykjavik", country= "Iceland")
geo1 = describe_city(city="Paris")
print(f"{geo[0]} is in {geo[1]}")
print(f"{geo1[0]} is in {geo1[1]}")


import random

def num(guess_num):
    secret_num = random.randint(1, 100)
    
    if guess_num == secret_num:
        print("Success! (if the numbers match)")
    else:
        print(f"Fail! Your number: {guess_num}, Random number: {secret_num} (if they don't match)")
num(78)    

def make_shirt(size= "large", text= "I love python"):
    return size, text

shirt_size = make_shirt(size="Medium", text="Your shirt size is Medium")
shirt_large = make_shirt(size="Large")
shirt_medium = make_shirt(size="Medium")


print(shirt_size)
print(shirt_large)
print(shirt_medium)


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):

    for name in magician_names:
        print(name)
show_magicians(magician_names)

def make_great(magician_names):
    for name in magician_names:
        print(name +" " + "The great")
make_great(magician_names)


def get_random_temp():
    return random.randint(-10, 40)


def main():
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature}°C")
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temperature in range(0,16):
        print("Quite chilly! Don’t forget your coat.")
    elif temperature in range(16,23):
        print("Nice weather.")
    elif temperature in range(24,32):
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool")
              

    

main()

