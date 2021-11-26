import math
h1 = int(input("Kérem a háromszög első oldalát: "))
h2 = int(input("Kérem a háromszög első oldalát: "))
h3 = int(input("Kérem a háromszög első oldalát: "))
kerulet = h1 + h2 + h3
d = (h1+ h2+ h3) / 2
e = (d * (d - h1) * (d - h2) * (d - h3))
print("Kerület: ", kerulet)
print("Terület: ", math.sqrt(e))