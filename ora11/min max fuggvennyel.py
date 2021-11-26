import random


def maximum_kereses(lista: list[float]) -> float:
    """
    Megkeresi egy valós számokat tartalmazó listának a legnagyobb elemét.
    :param lista: Valós számok listája
    :return: A lista maximum értéke
    """
    max = lista[0]
    for number in lista:
        if max < number:
            max = number
    return max


def kiiratas(szam: float) -> None:
    print(szam)



numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))
print(numbers)

maximum = maximum_kereses(numbers)
print(maximum)
kiiratas(maximum_kereses(numbers))


min = numbers[0]
max = numbers[0]
for number in numbers:
    if min > number:
        min = number
    if max < number:
        max = number
print("min: ", min, "max: ", max)