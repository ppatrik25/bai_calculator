import random

print(random.randint(0, 400))
print(random.random())

a = random.randint(-100, 100)
print(a)
if a>0:
    print("a szám pozitiv")
elif a<0:
    print("a szám negativ")
else:
    print("a szám nulla")