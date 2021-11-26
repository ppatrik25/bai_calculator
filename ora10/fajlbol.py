try:
    fileobject = open("lorem.txt", "r")
    tartalom = fileobject.readlines()
    print(tartalom)
    print(type(tartalom))
    print(len(tartalom))
    print(fileobject.tell())
    fileobject.close()
except FileNotFoundError:
    print("Nem található a fájl.")


fileobject2 = open("lorem5.txt", "w")
fileobject2.write("Python")
fileobject2.flush()
fileobject2.write("Python")
fileobject2.close()