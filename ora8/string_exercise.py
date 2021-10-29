python = "python"
print("A python szó 1. karaktere:", python[0])
print("A python szó utolsó karaktere:", python[len(python)-1])
print("A python változóm 5-ször egymás után:", python*5)
str2 = "hallgató"
str3 = "Hiába a hegyni anyag, a hallgató gyorsan halad."
print(str2 in str3)
print(python in str3)
print(python[2:5])   # balrol zart jobbrol nyitott intervallum
print(python + str2 + str3)
str4 = "HALLGATÓ"
print(str4 in str2)
