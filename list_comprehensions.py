Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> Deepti verma.py
  File "<python-input-0>", line 1
    Deepti verma.py
           ^^^^^
SyntaxError: invalid syntax
>>> python 3
  File "<python-input-1>", line 1
    python 3
           ^
SyntaxError: invalid syntax
>>> pythin3 Deepti verma.py
  File "<python-input-2>", line 1
    pythin3 Deepti verma.py
            ^^^^^^
SyntaxError: invalid syntax
>>> python3 Deepti.py
  File "<python-input-3>", line 1
    python3 Deepti.py
            ^^^^^^
SyntaxError: invalid syntax
>>> deepti.py
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    deepti.py
    ^^^^^^
NameError: name 'deepti' is not defined
>>> a, b = 1,2
>>> a # 1
1
>>> b # 2
2
>>> cats = "meow"
>>> import pandas
Traceback (most recent call last):
  File "<python-input-9>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
>>> import pandas as pd
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
>>> pip install pandas openpyxl
...
  File "<python-input-11>", line 1
    pip install pandas openpyxl
        ^^^^^^^
SyntaxError: invalid syntax
The Python package manager (pip) can only be used outside of the Python REPL.
Try the 'pip' command in a separate terminal or command prompt.
>>> for x in "word"
  File "<python-input-12>", line 1
    for x in "word"
                   ^
SyntaxError: expected ':'
>>> for x in "word" print (x)
  File "<python-input-13>", line 1
    for x in "word" print (x)
                    ^^^^^
SyntaxError: invalid syntax
>>> for x in "word" :
...     print (x)
...     for x in "word":
...     print(x)
...
  File "<python-input-14>", line 4
    print(x)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 3
>>> for x in "word":
...     print(x)
...
w
o
r
d
>>> x = "my favourites" /
  File "<python-input-16>", line 1
    x = "my favourites" /
                         ^
SyntaxError: invalid syntax
>>> x = "my favorite" \
... "string"
>>> new_str = "hello"
>>> for c in "world":
...     new_str += c
...     print(new_str)
...
hellow
hellowo
hellowor
helloworl
helloworld
>>> print("my name is Deepti")
my name is Deepti
>>> name = "Deepti"
>>> age = 30
>>> print(name)
Deepti
>>> print(age)
30
>>> score = 10
>>> score = 15
>>> print(score)
15
>>> score = score + 5
>>> print(score)
20
>>> city = rehovot
Traceback (most recent call last):
  File "<python-input-30>", line 1, in <module>
    city = rehovot
           ^^^^^^^
NameError: name 'rehovot' is not defined
>>> city = "rehovot"
>>> Print(city)
Traceback (most recent call last):
  File "<python-input-32>", line 1, in <module>
    Print(city)
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print(city)
rehovot
>>> apples = 5
>>> print (apples)
5
>>> print (apples) + 3
5
Traceback (most recent call last):
  File "<python-input-36>", line 1, in <module>
    print (apples) + 3
    ~~~~~~~~~~~~~~~^~~
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> apples = apples + 3
>>> print(apples)
8
>>> print(5 + 5)
10
>>> print("5" + "5")
55
>>> print(str(5) + "apples")
5apples
>>> print(10 == 3)
False
>>> print(10 != 3)
True
>>> instructor = 'elie'
>>> instructor.find('e')
0
>>> instructor.find('E')
-1
>>> string.find("i")
Traceback (most recent call last):
  File "<python-input-47>", line 1, in <module>
    string.find("i")
    ^^^^^^
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> string.find('i')
Traceback (most recent call last):
  File "<python-input-48>", line 1, in <module>
    string.find('i')
    ^^^^^^
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> string.isalpha()
Traceback (most recent call last):
  File "<python-input-49>", line 1, in <module>
    string.isalpha()
    ^^^^^^
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> "awesome".partition('e')
('aw', 'e', 'some')
>>> user = 'Deepti'
>>> if user == 'Deepti'
  File "<python-input-52>", line 1
    if user == 'Deepti'
                       ^
SyntaxError: expected ':'
>>> if user == 'Deepti':
...     print ('Awesome!')
...     elif user == 'Tom':
...         print('Cool')
...         else:
...             print('Nope')
...
  File "<python-input-53>", line 3
    elif user == 'Tom':
    ^^^^
SyntaxError: invalid syntax
>>> elif user == ('Tom'):
  File "<python-input-54>", line 1
    elif user == ('Tom'):
    ^^^^
SyntaxError: invalid syntax
>>> if user == 'Deepti':
... ...     print ('Awesome!')
... ...     elif user == ('Tom'):
... ...         print('Cool')
... ...         else:
... ...             print('Nope')
...
  File "<python-input-55>", line 2
    ...     print ('Awesome!')
    ^^^
IndentationError: expected an indented block after 'if' statement on line 1
>>> user = 'Elie'
... if user == 'Elie':
...     print('Awesome!')
... elif user == 'Tom':
...     print('Cool!')
... else:
...     print('Nope!')
...
Awesome!
>>> if 1 > 2 or 2 > 1:
...     print('cool')
...     if 1 == 1 and 2 == 2:
...         print('nice')
...         if not  false:
...             print('It is true')
...
cool
nice
Traceback (most recent call last):
  File "<python-input-57>", line 5, in <module>
    if not  false:
            ^^^^^
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> if 1 > 2 or 2 > 1:
...     print('cool')
...     if 1 == 1 and 2 == 2:
...         print('nice')
...         if not  False:
...             print('It is true')
...
cool
nice
It is true
>>> if 1 < 2  and 2 < 3:
...     print("this is ok")
...     if 1 < 2 < 3:
...         print("this is better")
...
this is ok
this is better
>>> name = "Matt"
>>> if name == "Matt":
...     print("Your name is Matt")
...     print("Bye")
...
Your name is Matt
Bye
>>> name = "Matt"
... if name == "Matt":
... print("Your name is Matt")
...
  File "<python-input-62>", line 3
    print("Your name is Matt")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
>>> first = "Ada"
... last = "Lovelace"
... full = first + " " + last
... print(full)            # Ada Lovelace
... print(len(full))       # 12
... print(full.upper())    # ADA LOVELACE
... print(full.lower())    # ada lovelace
...
Ada Lovelace
12
ADA LOVELACE
ada lovelace
>>> name = "Ada"
... items = 3
... price = 4.5
... print(f"{name} bought {items} items for {items * price} in total")
...
Ada bought 3 items for 13.5 in total
>>> name = input("What is your name? ")
... print(f"Nice to meet you, {name}!")
...
What is your name?
Nice to meet you, !
>>> name = "Deepti"
>>> name = input("What is your name? ")
... print(f"Nice to meet you, {name}!")
...
What is your name?
Nice to meet you, !
>>> name = input("What is your name? ")
...
What is your name?
>>>
>>> first = "Hello World" # This is a comment
>>> input("I am a computer")
I am a computer
''
>>> if 1 < 2  and if 4 > 2:
  File "<python-input-72>", line 1
    if 1 < 2  and if 4 > 2:
                  ^^
SyntaxError: invalid syntax
>>> if 1 < 2  and 4 > 2:
...     print("Math is fun")
...
Math is fun
>>> string.uppercase = ("i am shouting")
Traceback (most recent call last):
  File "<python-input-74>", line 1, in <module>
    string.uppercase = ("i am shouting")
    ^^^^^^
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> text = 'i am shouting'
>>> print (text.upper())
I AM SHOUTING
>>> num = 1000
>>> string.num()
Traceback (most recent call last):
  File "<python-input-78>", line 1, in <module>
    string.num()
    ^^^^^^
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> text = "1000"
>>> number = int(text)
>>> print(number)
1000
>>> print(number +1)
1001
>>> text = "real"
>>> print(4 + text)
Traceback (most recent call last):
  File "<python-input-84>", line 1, in <module>
    print(4 + text)
          ~~^~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print("4" + real)
Traceback (most recent call last):
  File "<python-input-85>", line 1, in <module>
    print("4" + real)
                ^^^^
NameError: name 'real' is not defined
>>> print("4" + text)
4real
>>> values = [1,2,3,4,5]
>>> for val in values:
...     print(val)
...
1
2
3
4
5
>>> for car in "awesome":
...     print car
...
  File "<python-input-89>", line 2
    print car
    ^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> for char in "awesome":
...     print(char)
...
a
w
e
s
o
m
e
>>> for idx, char in enumerate("awesome):
  File "<python-input-91>", line 1
    for idx, char in enumerate("awesome):
                               ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print(idx,char)
Traceback (most recent call last):
  File "<python-input-92>", line 1, in <module>
    print(idx,char)
          ^^^
NameError: name 'idx' is not defined. Did you mean: 'id'?
>>> print(idx, char)
Traceback (most recent call last):
  File "<python-input-93>", line 1, in <module>
    print(idx, char)
          ^^^
NameError: name 'idx' is not defined. Did you mean: 'id'?
>>> for idx, in char in enumerate("awesome"):
...     print(idx, char)
...
Traceback (most recent call last):
  File "<python-input-94>", line 1, in <module>
    for idx, in char in enumerate("awesome"):
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'bool' object is not iterable
>>> for idx, char in enumerate("awesome"):
...     print(idx, char)
...
0 a
1 w
2 e
3 s
4 o
5 m
6 e
>>> word = "cat"
>>> for i, char in enumerate(word):
...     print(i, word)
...
0 cat
1 cat
2 cat
>>> print(i, char)
2 t
>>>
>>> word = "cat"
...
... for i, char in enumerate(word):
...     print(i, char)
...
0 c
1 a
2 t
>>> student = "deepti", "Barry", "Leeroy", "Steven"
>>> for idx, char in enumerate(student):
...     print(idx, char)
...
0 deepti
1 Barry
2 Leeroy
3 Steven
>>> for idx, char in enumerate(student, start=1):
...     print(idx, char)
...
1 deepti
2 Barry
3 Leeroy
4 Steven
>>> count = 0
>>> for char in "education":
...     if char in "aeiou":
...         count = count + 1
...         print(count)
...
1
2
3
4
5
>>> for char in "python":
...     print(char)
...
p
y
t
h
o
n
>>> for i, char in "python":
...     print(i, char)
...
Traceback (most recent call last):
  File "<python-input-107>", line 1, in <module>
    for i, char in "python":
        ^^^^^^^
ValueError: not enough values to unpack (expected 2, got 1)
>>> for i, char in enumerate"python", start=1):
...     print(i, char)
...
  File "<python-input-108>", line 1
    for i, char in enumerate"python", start=1):
                                             ^
SyntaxError: unmatched ')'
>>> for i, char in enumerate("python", start=1):
...     print(i, char)
...
1 p
2 y
3 t
4 h
5 o
6 n
>>> for fruit, char in "banana":
...     if == "a":
...         count = count +1
...         print(count)
...
  File "<python-input-110>", line 2
    if == "a":
       ^^
SyntaxError: invalid syntax
>>> for fruit, char in "banana":
...     if char == "a":
...         count = count +1
...         print(count)
...
Traceback (most recent call last):
  File "<python-input-111>", line 1, in <module>
    for fruit, char in "banana":
        ^^^^^^^^^^^
ValueError: not enough values to unpack (expected 2, got 1)
>>> for fruit, char in "banana":
...     if char == "a":
...         count = count +1
...         print(fruit)
...
Traceback (most recent call last):
  File "<python-input-112>", line 1, in <module>
    for fruit, char in "banana":
        ^^^^^^^^^^^
ValueError: not enough values to unpack (expected 2, got 1)
>>> for char in "banana":
...     if char == "a":
...         count = count +1
...         print(count)
...
6
7
8
>>> print(char)
a
>>> capital_letters = []
... for num in range(65,91):
...     capital_letters.append(chr(num))
...
>>>
>>> capital_letters
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
>>> [num**2 for num in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [chr(num) for num in range(65,91)]
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
>>> print(ord("A"))
65
>>> chr(100)
'd'
>>> char(92)
Traceback (most recent call last):
  File "<python-input-122>", line 1, in <module>
    char(92)
    ~~~~^^^^
TypeError: 'str' object is not callable
>>> chr(92)
'\\'
>>> vowels = []
>>> for letter in 'awesome':
...     if letter in ['a' , 'e', 'i', 'o', 'u']:
...         vowels.append(letter)
...
>>> print(vowels)
['a', 'e', 'o', 'e']
>>> len([word for word in "the quick brown fox jumps over the lazy dog".split(" ") if len(word) == 3])
...
4
>>> import string
... print(string.ascii_lowercase)
...
abcdefghijklmnopqrstuvwxyz
>>> import pandas as pd
... import numpy as np
...
>>>
>>>
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

>>> numbers = [1,2,3,4]
>>> print([x for x in numbers])
[1, 2, 3, 4]
>>> print([x*20 for x in numbers])
[20, 40, 60, 80]
>>> name =  [“Elie”, “Tim”, “Matt”]
  File "<python-input-136>", line 1
    name =  [“Elie”, “Tim”, “Matt”]
             ^
SyntaxError: invalid character '“' (U+201C)
>>> name =  [“Elie”, “Tim”, “Matt”]:
  File "<python-input-137>", line 1
    name =  [“Elie”, “Tim”, “Matt”]:
             ^
SyntaxError: invalid character '“' (U+201C)
>>> name = “Elie”, “Tim”, “Matt”
  File "<python-input-138>", line 1
    name = “Elie”, “Tim”, “Matt”
           ^
SyntaxError: invalid character '“' (U+201C)
>>> name = ["Elie", "Tim", "Matt"]
>>> first_letter = [name(0) for name in name]
Traceback (most recent call last):
  File "<python-input-140>", line 1, in <module>
    first_letter = [name(0) for name in name]
                    ~~~~^^^
TypeError: 'str' object is not callable
>>> first_letter = [name[0] for name in name]
>>> print(first_letter)
['E', 'T', 'M']
>>> number =  [1,2,3,4,5,6]
>>> evens = [n for n in numbers if n % 2 == 0]
>>> print(evens)
[2, 4]
>>> list_a = [1, 2, 3, 4]
... list_b = [3, 4, 5, 6]
...
... common = [x for x in list_a if x in list_b]
... print(common)
...
[3, 4]
>>> print(list(set(list_a) & set(list_b)))
[3, 4]
>>> names = ["Ellie", "tim", "Matt"]
>>> result = [for name in names name [::-1].lower()]
  File "<python-input-149>", line 1
    result = [for name in names name [::-1].lower()]
              ^^^
SyntaxError: invalid syntax
>>> result = [ name[::-1].lower() for name in names]
>>> print(result)
['eille', 'mit', 'ttam']
>>> number = range(1,100)
>>> division = [n for n in number if n % 12 == 0]
>>> print(division)
[12, 24, 36, 48, 60, 72, 84, 96]
>>>  string = "amazing"
  File "<python-input-155>", line 1
    string = "amazing"
IndentationError: unexpected indent
>>> name = 'amazing'
>>> consonants = [char for char in name if char not in "aeiou"]
... print(consonants)
...
['m', 'z', 'n', 'g']
>>> matrix = [[i for i in range(3)] for _ in range(3)]
... print(matrix)
...
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
>>> matrix = [[i for i in range(10)] for _ in range(10)]
... print(matrix)
...
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]