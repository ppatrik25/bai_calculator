number = 5
print("A number változó értéke:", number, "\b. Ha megszorzom kettővel, akkor:", number*2, "\b-t kapunk.")
print("A number változó értéke: ", number, ". Ha megszorzom kettővel, akkor: ", number*2, "-t kapunk.", sep="")
print(f"A number változó értéke: {number}. Ha megszorzom kettővel, akkor: {number*2}-t kapunk.")
print("A number változó értéke: {}. Ha megszorzom kettővel, akkor: {}-t kapunk.".format(number, number*2))

# Igazítások

print(f"A number változó értéke: {number:<3}. Ha megszorzom kettővel, akkor: {number*2:<3}-t kapunk.")
print("A number változó értéke: {:^5}. Ha megszorzom kettővel, akkor: {:^4}-t kapunk.".format(number, number*2))

# Számformátum

number = 13
print(f"A number változó bináris értéke: {number:b}.")
print("A number változó oktális értéke: {:o}.".format(number))
print(f"A number változó decimális értéke: {number:d}.")
print("A number változó hexadecimális értéke: {:x} és {:X}.".format(number, number))

# Unicode

#

# Valós számok
number = 100.1232                   #TÖBBI CSEKOK REPOSITORYBAN