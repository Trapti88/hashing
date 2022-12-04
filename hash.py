import random

uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

marks = "0123456789"

symbols = "!@#$%^&*<>?|\\()/,.{}"

you=input("What your password")

upper,lower,dig,syms = True, True, True, True

all = ""

if upper:
    all +=uppercase_letters

if lower:
    all +=lowercase_letters

if dig:
    all +=marks 

if syms:
    all += symbols

length =20

amount = 10

for x in range(amount):
    passsword = "".join(random.sample(all,length))
    f"(password)"

