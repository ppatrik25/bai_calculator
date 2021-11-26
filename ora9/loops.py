is_number = False
number = 0
while not is_number:
    try:
        number = int(input("Kérek egy egész számot: "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")

if number % 2 == 0:
    print("páros")
else:
    print("páratlan")

i = 1
while i <= 5:
    print(i)
    i += 1
print()

for j in [1, 2, 3, 4, 5]:
    print(j)
print()

for k in range(100):
    print(k, end=" ")
print()

for l in range(50, 60):
    print(l)
print()

for l in range(10):
    print(l + 50)
print()

for n in range(101):
    if (n % 2 != 0):
        print(n)