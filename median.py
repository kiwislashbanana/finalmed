import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

def mediana(mass1, mass2):
    if not isinstance(mass1, list) or not isinstance(mass2, list):
        logging.error("Ошибка: параметры не списки")
        raise TypeError("Засунь списки")

    mass3 = sorted(mass1 + mass2)
    nums = len(mass3)
    if nums == 0:
        logging.error("ValueError: оба массива пустые")
        raise ValueError("Both arrays are empty")

    med = nums // 2
    if nums % 2 == 0:
        return (mass3[med - 1] + mass3[med]) / 2
    else:
        return mass3[med]


mass1 = [2, 7, 2, 8, 2]
mass2 = [5, 1, 9, 10, 6]
print(mediana(mass1, mass2))
