def main():
    global money, playGame

    money = loadMoney()
    startMoney = money

    while(playGame and money > 0):
        #colorLine(10, "Приветствую тебя в нашем казино, дружище!)
        #color(14))
        print(f" У тебя на счету {money} {valuta}")

        #color(6)
        print("""Ты можешь сыграть в:
                       1. Рулетку
                       2. Кости
                       3. Однорукого бандита
                       
                       0. Выход. Ставка 0 в играх - выход.""")
        color(7)



def getInput(digit, message):   # Функция ввода значения
    color(7)
    ret = ""
    while(ret == "" or not ret in digit):
        ret = input(message)
    return ret
def getIntInput(minimum, maximum, message):   # Функция ввода целого числа
    #color(7)
    ret = -1
    while(ret < minimum or ret > maximum):
        st = input(message)
        if (st.isdigit()):
            ret = int(st)
        else:
            print("    Введите целое число!")
    return ret
a = getIntInput(0, 10, "Введите от 0 до 10: ")
print(a)

def loadMoney():   # Загрузка из файла денег
    pass
def saveMoney():   # Сохранение в файл денег
    pass
def color():   # Установка цвета денег
    pass
def colorLine(c, s):   # Обрамление в цветную рамку из звездочек
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))
def roulette():   # Метод рулетки
    pass
def getRoulette(visible):   # Функция рулетки
    pass
def dice():   # Метод костей
    pass
def getDice():   # Функция костей
    pass
def oneHandBanditRes(stavka):   # Метод однорукого бандита
    pass
def getMaxCount(digit, v1, v2, v3, v4 ,v5):   # Функция однорукого бандита
    pass
def pobeda(result):   #Вывод сообщения о выигрыше
    pass
def proigr(result):   # Вывод сообщения о проигрыше
    pass
