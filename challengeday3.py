week1/user = input("Enter a word:")
letters = {}
for i, letter in enumerate(user):
  
  if letter in letters:
    letters[letter].append(i)
  else:
    letters[letter] = [i]
print(letters)


items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

basket = []
wallet = wallet.replace("$", "")  
wallet = wallet.replace(",", "")
wallet = int(wallet)

for item, price in items_purchase.items():
    price = price.replace("$", "")
    price = price.replace(",", "")
    price = int(price)

    if price <= wallet:
      basket.append(item)  
      wallet = wallet - price

if basket == []:
    print("Nothing")
else:
    print(sorted(basket))


items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"
print(list(items_purchase.keys()))


items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
items_purchase = {}
print("Nothing")

