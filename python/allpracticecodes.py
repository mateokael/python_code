from prettytable import PrettyTable
import random
import math
lists = ["q", "W", "E", "q", ['tngnna', 'qaq']]

# count
lists.count('q')
# add item at the end
lists.append("gqgo")
# insert at specified index
lists.insert(2, 'tnginaa')
# remove delete value
lists.remove("q")
# pop specific index pag none equals dulo
lists.pop(0)
# del index if none deletes all

# clear deletes all
# lists.clear()
# copy whole list
x = lists.copy
print(x)
# reverse
lists.reverse()
# sort
# lists.sort()  # AscendingORDER
# lists.sort(reverse=True)  # descending
# NESTED lists inside a lists


# print
print(lists)
# read list index
print(lists[1])
# range
print(lists[:3])
# length
len(lists)


# String
"titi"

# Integer
12345

# Float
1.23

# Boolean
True
False


first = "lance"
last = "pogi"
all = f"{first} {last}"
print(all)


course = "lance mathew"
print(course.title())
print(course)
print(course.strip())


print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

# primitive types
int(x)
float(x)
bool(x)
str(x)


x = input("x: ")
y = int(x)+1
# y = x + 1
print(f"x: {x}, y: {y}")

# Falsy
# ""
# 0
# None


age = int(input())

if 12 == age <= 18:
    print("ok")

elif age < 12:
    print("not ok")

else:
    print("okok")

pogi = 1
if pogi > 50:
    print("ok")

elif pogi > 20:
    print("not ok")

else:
    print("gg")


high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("eligible")
else:
    print('not')


# age should between 18 and 65
age = int(input("drop your age: "))

if 18 <= age < 65:
    print("enter")
else:
    print('no')


count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even no.s")


if 10 == '10':
    print("a")
elif "bag" > 'apple' and 'bag' > 'cat':
    print('b')
else:
    print('c')


# 1st proj

input("would you like to run this program?(type yes to continue else discard) ")
if "yes":
    firstname = input("your first name?  ")
    secondname = input("your last name? ")
    print("this is your name:" + firstname + " " + secondname)

else:
    print("thank you for your considerations")


# attempts (loop)
s = False

for number in range(3):
    print("ATTEMPT", number + 1)
    if s:
        print("SUCCESS")
        break
else:
    print("attempted 3 times bur fAILED")

# NESTED LOOPS
for x in range(5):
    for y in range(3):
        print(f"{x},{y}")


# Iterable
for x in "Python":
    print(x)

for y in range(5):
    print(y)


# Y loop

number = 100
while number > 0:
    print(number)
    number //= 2


command = ''
while command.lower() != 'quit':
    command = input(">")
    print("ECHO", command)


# 2nd project

two_digit_number = input()

x = int(two_digit_number[0])

y = int(two_digit_number[1])

two_digit_number = x + y

print(two_digit_number)

# 3rd project BMI CALCU

height = input()
weight = input()

h = float(height)

w = int(weight)

result = w / (h ** 2)

print(int(result))


# 4th project weeks left in life
age = input()
x = int(age)
y = 4700 - x * 52

print(f"You have {y} weeks left")

# 2nd day proj tip calcu
Total = float(input('Your total is: '))

Tip = float(input("pick your tip percentage? 10 20 15 "))

Split = float(input("How many people to split the bill? "))


x = Tip / 100
y = Total * x
result = y + Total
all = result / Split
all2 = round(all, 2)

print(f"Your final total is {all2}")


# odd or even
number = int(input())

if number % 2 == 0:
    print("even")

else:
    print("odd")

# BMi 2

height = input("height: ")
weight = input("weight: ")

h = float(height)

w = float(weight)

result = w/(h ** 2)

if 18.5 >= result < 25:
    print("normal")
elif 25 <= result < 30:
    print("slighty over")
elif 30 <= result < 35:
    print("obese")
elif 35 <= result:
    print("clinically obese")
else:
    print("underweight")

print(result)

if result < 18.5:
    print("under")
elif result < 25:
    print("normal")
elif result < 30:
    print("slightly")
elif result < 35:
    print(" obese")
else:
    print("clinically")

# LEAP YEARCHECKER
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap")
        else:
            print("not")
    else:
        print("leap")
else:
    print("not")

# ticket
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        z = 5
        print("Child tickets are 5$")
    elif age <= 18:
        z = 7
        print("7$")
    elif 45 <= age <= 55:
        print('ok')
    else:
        z = 12
        print("12")

    photo = input("Do you want photos?")
    if photo == "yes":
        z += 3
    print(z)
else:
    print("sorry, you cant ride")


# PIZZA ordder
print("thank you")
size = input()
add_pepperoni = input()
extra_cheese = input()
z = 0


if size == "S":
    z += 15
    if add_pepperoni == "Y":
        z += 2
elif size == "M":
    z += 20
    if add_pepperoni == "Y":
        z += 3
elif size == "L":
    z += 25
    if add_pepperoni == "Y":
        z += 5

if extra_cheese == "Y":
    z += 1

print(f'your final bill is {z}')


# love calcu
name1 = input()
name2 = input()

combined = name1 + name2

low = combined.lower()

t = low.count('t')
r = low.count("r")
u = low.count('u')
e = low.count("e")

true = t + r+u+e

l = low.count("l")
o = low.count("o")
v = low.count("v")
e = low.count("e")

love = l+o+v+e

lovestr = str(love)
truestr = str(true)
all = truestr+lovestr

print(all)

allstr = int(all)

if allstr <= 10:
    print('nooo')
if 11 <= allstr <= 89:
    print('not bad')
else:
    print("great")


# My attempt
lovestr = str(love)
truestr = str(true)
all = truestr+lovestr
allstr = int(all)
# shorterway
all = int(str(true)+str(love))
{all}


# day3 proj if elif else
print("find the treasure")
way = input("go left or go right")


if way == "right":
    print("gameover")
else:
    wait = input("swim or wait")
    if wait == "swim":
        print("gameover")
    else:
        door = input("pick a door; blue, red, yellow")
        if door == "blue":
            print('gameover')
        elif door == "red":
            print('gameover')
        elif door == "yellow":
            print('You win')


# random

nteger = random.randint(1, 10)
print(nteger)

flot = random.random()
print(flot)

print(flot + nteger)

# random heads tails

randomint = random.randint(1, 2)

if randomint == 1:
    print("Heads")
else:
    print('Tails')


# randomiser names input string

names = ('a', 'c', 'd', 'e')
alln = len(names)
randnumber = random.randint(0, alln - 1)
print(names[randnumber])


x = ['o', 'o', 'o']
y = ['o', 'o', 'o']
z = ['o', 'o', 'o']
xyz = [x, y, z]
print('treasure')
position = input()

if position == 'A1':
    x.pop(0)
    x.insert(0, "X")

if position == 'B1':
    x.pop(1)
    x.insert(1, "X")

if position == 'C1':
    x.pop(2)
    x.insert(2, "X")


if position == 'A2':
    y.pop(0)
    y.insert(0, "X")

if position == 'B2':
    y.pop(1)
    y.insert(1, "X")

if position == 'C2':
    y.pop(2)
    y.insert(2, "X")


if position == 'A3':
    z.pop(0)
    z.insert(0, "X")

if position == 'B3':
    z.pop(1)
    z.insert(1, "X")

if position == 'C3':
    z.pop(2)
    z.insert(2, "X")


print(f'{x}\n{y}\n{z}')

or

x = ['o', 'o', 'o']
y = ['o', 'o', 'o']
z = ['o', 'o', 'o']
xyz = [x, y, z]
print('treasure')
position = input()

letter = position[0].lower()
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

xyz[number_index][letter_index] = 'X'


print(f'{x}\n{y}\n{z}')


# ROCK PAPER SCISSOR 4th day project (no help)

player = int(input())
if player > 2 or player < -2:
    print('invalid number ni-')
    exit()
rps = ['rock', 'paper', 'scissor']
computer = random.choice(rps)
indexcomp = rps.index(computer)
print(rps[player])
print(computer)

# paper and rock, scissor and paper
if player - indexcomp == 1:
    print("player wins")
# rock and paper, paper and scissor
elif player - indexcomp == -1:
    print("computer wins")
# rock and scissor
elif player - indexcomp == -2:
    print('player wins')
# scissor and rock
elif player - indexcomp == 2:
    print('computer wins')
# pagparehas
else:
    print('draw')


# height calculator
heights = input().split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])

total = 0
for height in heights:
    total += height
average = total / (n+1)
print((n+1))
print(total)
print(average)
# or use this para mabilang ilan dumaan sa loop
number = 0
for student in heights:
    number += 1


# high score
scores = input().split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

high = 0
for score in scores:
    if score > high:
        high = score
print(high)

# sum calcu
target = int(input())

total = 0
for number in range(0, target + 1, 2):
    total += number
print(total)
# or
# for number in range(0, target + 1):
#   if number % 2 == 0:
#       total += number

# fizzbuzz
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# password generator

# All letters (lowercase + uppercase) as strings
letters = ['a', 'b', 'c', 'd']  # ['a', 'b', ..., 'Z']

# All digits 0-9 as strings
numbers = ['1', '2', '3', '4']       # ['0', '1', ..., '9']

# 10 common symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

nrletters = int(input())
nrnumbers = int(input())
nrsymbols = int(input())


p = []
for char in range(1, nrletters + 1):
    a = random.choice(letters)
    p.append(a)
for char in range(1, nrnumbers + 1):
    a = random.choice(numbers)
    p.append(a)
for char in range(1, nrsymbols + 1):
    a = random.choice(symbols)
    p.append(a)

password = ''

for char in range(0, len(p)):
    password += random.choice(p)

print(password)

# paint


def paint_calc(height, width, cover):
    print(math.ceil((height * width) / cover))


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# PRIME NUMBER CHECKER
def prime_checker(number):
    if number < 2:
        print("not")
        return

    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("PRIME")
    else:
        print("not")


n = int(input())
prime_checker(number=n)

# hangman


words = ["candle", "river", "shadow", "whisper", "planet",
         "breeze", "mirror", "storm", "galaxy", "feather", "nigga", "tanginamo", "gago"]

rword = random.choice(words)

# answer print(rword)


hidden = ['_', "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_", "_",]


numword = len(rword)
print(" ".join(hidden[0:numword]))
hid = hidden[0:numword]

y = 6
while '_' in hid:
    guess = input().lower()
    x = -1
    found = False
    for letter in rword:
        x += 1
        if guess == letter:
            hid[x] = guess
            found = True

    if not found:
        y -= 1
        print(f'you have {y} lives. ')
        if y == 0:
            print("You Lose")
            break

    print(" ".join(hid))
if '_' not in hid:
    print("You Win")


# caesar encrypt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("encode to encrypt, decode to decrypt:\n")
text = input("message here:\n").lower()
shift = int(input("shift number:\n"))


def caesar(plain_text, shift_amount):

    if direction == "encrypt":
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(cipher_text)

    if direction == "decrypt":
        decipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            letter2pos = (position - shift_amount)
            newletter2 = alphabet[letter2pos]

            decipher_text += newletter2
        print(decipher_text)


caesar(plain_text=text, shift_amount=shift)


# or

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continu = True
while continu:
    direction = input("encode to encrypt, decode to decrypt:\n")
    text = input("message here:\n").lower()
    shift = int(input("shift number:\n"))

    def caesar(plain_text, shift_amount, direc):

        end_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if direc == "decrypt":
                    shift_amount *= -1
                letterpos = (position + shift_amount) % 26
                end_text += alphabet[letterpos]

                if direc == "decrypt":
                    shift_amount *= -1
            else:
                end_text += letter

        print(end_text)
    caesar(plain_text=text, shift_amount=shift, direc=direction)
    result = input("again or no: ")
    if result == 'no':
        continu = False


# dictionaries
programming_dictionary = {
    "Bug": "tningangyan",
    "Function": "pangqaqo",
}

print(programming_dictionary["Bug"])

# adding
programming_dictionary["Loop"] = 'qaqo'

# wipe and exist
programming_dictionary = {}


# edit
programming_dictionary["Bug"] = "pangqaqo"

# loop through
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# DICTIO

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds"
    elif 71 <= score <= 80:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# travel log
# Nesting List in a Dictionaty

travel_log = {
    "france": ["Paris", "Lille"],
    "germany": ["berlin", "hamburg"]
}
# dict in dict
travel_log = {
    "france": {"cities visited": ["Paris", "Lille"], "total visits": 12},
    "germany": {"cities in germany": ["berlin", "hamburg"], "visits": 11}
}

# dict in a list
travel_log = [
    {
        "country": "france",
        "cities visited": ["Paris", "Lille"],
        "total visits": 12},
]

print(travel_log[0])


# travellop
travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities": ["Paris", "Lille"],
    },
]


def add_new_country(country, visits, list_of_cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    })


conti = True
while conti:
    country = input()
    visits = int(input())
    list_of_cities = eval(input())

    add_new_country(country, visits, list_of_cities)

    print(
        f"ive been to {travel_log[-1]["country"]} {travel_log[-1]['visits']} times.")

    print(f"my fave city was {travel_log[-1]["cities"][0]}")

    g = input('would you like to add one more? ').lower()
    if g == "no":
        conti = False
print('FUll travel log: ')
for entry in travel_log:
    print(entry)


# secretbidding
names = {


}

highbid = {
    'name': '',
    'bid': 0
}


def bidders():
    for bids in names:
        score = names[bids]
        if score > highbid['bid']:
            highbid['name'] = name
            highbid['bid'] = bid


cont = True
while cont:
    name = input("name? ")
    bid = int(input())
    ques = input("type yes or no ").lower()

    names[name] = bid
    bidders()

    if ques == "yes":
        print('kunyare naclear tngina')
    else:
        print(f' name: {highbid['name']} bid {highbid['bid']}')
        cont = False

# Functions with Outputs


def format_name(f_name, l_name):
    x = f_name.title()
    y = l_name.title()
    return f"{x} {y}"


print(format_name("qaqo", 'QAQu'))

# days in month


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return print(29)
    else:
        return month_days[month  12 - 1]


year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)

# bascalc


def plus(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def times(n1, n2):
    return n1 * n2


ops = {
    "+": plus,
    "-": minus,
    "/": divide,
    "*": times

}

num1 = int(input("first numer: "))

con = True
while con:
    for sym in ops:
        print(sym)

    opsymbol = input("pick symbol: ")

    num2 = int(input("second number: "))

    calfunc = ops[opsymbol]
    first_answer = calfunc(num1, num2)

    print(f"{num1} {opsymbol} {num2} = {first_answer}")

    again = input("would you like to continue with your number? y or exit ")
    if again == "exit":
        con: False
    num1 = first_answer

# lucky12 ewan kung ano tawag jan
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def randomiser():
    return random.choice(numbers)


def computer():
    print(z, c)
    comfinal = z + c
    if comfinal > 12:
        comnum = comfinal % 12
        if final > comnum:
            print("you win")
        elif comnum > final:
            print("you lose")
        else:
            print("draw")

    elif final > comfinal:
        print("you win")
    elif comfinal > final:
        print("you lose")
    else:
        print("draw")


start = input("start game? y or n")
if start == "y":
    x = randomiser()
    y = randomiser()

print(f"{x}, {y} are your number")

z = randomiser()
c = randomiser()

print(f"{z} is computers number")

draw = input("draw your third number? y or n ")
if draw == "y":
    v = randomiser()
    finals = x + y + v
    if finals > 12:
        final = finals % 12
        print(f"your numbers {x},{y},{v}")
        computer()

    else:
        final = x + y + v
        print(x, y, v)
        computer()
else:
    final = x + y
    print(x, y)
    computer()


# highorlow

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 620,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 380,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'National Geographic',
        'follower_count': 260,
        'description': 'Nature and science magazine',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 350,
        'description': 'Reality TV star and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 490,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'NASA',
        'follower_count': 100,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 420,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'YouTube',
        'follower_count': 280,
        'description': 'Video sharing platform',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 400,
        'description': 'Reality TV star and entrepreneur',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 390,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
]

# def more():

comparelist = []


def nextround():

    for i in range(1):
        number_choice = random.randint(0, len(data) - 1)
        pickeddata = data[number_choice]
        comparelist.append(pickeddata)
        data.pop(number_choice)


# def results():
#     print(comparelist[0]['follower_count'], comparelist[1]['follower_count'])

def folwcount():
    for label, item in zip(labels, comparelist):
        print(f"{label}: {item["follower_count"]}")


for i in range(2):
    nextround()

again = True
while again:
    labels = ["A", "B"]
    for label, item in zip(labels, comparelist):
        print(
            f"{label}: {item["name"]}, {item["description"]}, {item["country"]}")

    answer = input("which has more followers? a or b")
    if answer == "a":
        if comparelist[0]['follower_count'] > comparelist[1]['follower_count']:
            print("NextRound")
            folwcount()
            comparelist.pop(1)
            nextround()

        else:
            print("YouLose")
            folwcount()
            again = False
    else:
        if comparelist[1]['follower_count'] > comparelist[0]['follower_count']:
            print("NextRound")
            folwcount()
            comparelist.pop(0)
            nextround()

        else:
            print("YouLose")
            folwcount()
            again = False
    if not data:
        print("You Win")
        again = False

# coffee machine
Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

Status = {
    "water": 0,
    "coffee": 1000,
    "milk": 1000,
}
Money = 0


def report():
    if start == "report":
        for item in Status:
            print(f"{item}:{Status[item]}")
        print(f"Money: {Money}")


def refill():
    for item in Status:
        Status[item] += 500

# def stockcheck():
#     missingitem = []
#     for ing, items in zip(Menu[start]["ingredients"], Status):
#         if ing < items:
#             missingitem.append(ing)

#     if missingitem:
#         print("Sorry, not enough of:")
#         for i in missingitem:
#             print(f"- {i}")


def money(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickels * 0.05
    total += pennies * 0.01
    return round(total, 2)


goagain = True
while goagain:
    start = input("What would you like?(espresso/ latte/ cappucino): ")
    if start == "report":
        report()
        continue
    if start == 'refill':
        refill()
        continue
    if start not in Menu:
        print("Invalid choice. Please select a valid option.")
        continue

    missing = []
    for item, ing in zip(Status, Menu[start]['ingredients']):
        if Status[item] < Menu[start]['ingredients'][ing]:
            missing.append(ing)
    if missing:
        print(f'out of stocked items: {",".join(missing)}')
        continue

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    inserted = money(quarters, dimes, nickels, pennies)
    print(inserted)

    if inserted < Menu[start]['cost']:
        print(f"Not enough money. Refunding ${inserted}")
        continue

    for item, ing in zip(Status, Menu[start]['ingredients']):

        if Status[item] >= Menu[start]['ingredients'][ing]:
            Status[item] -= Menu[start]['ingredients'][ing]

    change = inserted - Menu[start]['cost']
    print(f"your change is: {round(change, 2)}")
    Money += Menu[start]['cost']
    print(f"Here is your {start}")
    repeat = input("go again? y or n: ")
    if repeat == "n":
        goagain = False

# from turtle import Turtle, Screen
# x = Turtle()
# print(x)
# x.shape("turtle")
# x.color('coral')
# x.fd(200)
# x.right(90)
# x.fd(50)
# x.right(90)
# x.fd(200)
# x.left(90)
# x.fd(50)


# myscreen = Screen()
# print(myscreen.canvheight)
# myscreen.exitonclick()

table = PrettyTable()


table.add_column("tite", ["qaqo", "qao"])
table.add_column('gg', ['ss', 'qs'])

table.align = "r"

print(table)

# class User:
   def __init__(self, user_id, username
                 ):
        self.id = user_id
        self.useme = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('1', '2')
user_2 = User('q', 'e')


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
