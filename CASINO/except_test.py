try:
    f = open("???.txt", "r", encoding="utf-8")
    a = f.readline()
    f.close()
except IOError:
    print("Ошибка открытия")
    a = 0

def getInput1(digit, message):   # Функция ввода значения
    #color(7)
    ret = ""
    while ret == "" or not ret in digit:
        ret = input(message)
    return ret
print(f"Вы ввели число {getInput1('12', 'Введите число 1 или 2!')}")
