#    answer_base = {0: 00, 1: 1, 2: 2, 3: 10, 4: 11, 5: 12, 6: 20, 7: 21, 8: 22}
#    answer_base = {"00": 0, "01": 1, "02": 2, "10": 3, "11": 4, "12": 5, "20": 6, "21": 7, "22": 8}
#    answer_base = {'0': '00', '1': '01', '2': '02', '3': '10', '4': '11', '5': '12', '6': '20', '7': '21', '8': '22'}
#    print(answer_base)
#pole = [" 012", "0---", "1---", "2---"]

#game
print("gameXO")

pole = list("-"*9)

def drawpole2(pole):
    # отрисовка поля
    print("  0 1 2")
    for i in range(3):
        print(i, pole[0+i*3], pole[1+i*3], pole[2+i*3])
drawpole2(pole)

X2 = str('X')
def answer(X2):
    # проверка корректности ввода
    answer_correct = False
    answer_base = {0: "00", 1: "01", 2: "02", 3: "10", 4: "11", 5: "12", 6: "20", 7: "21", 8: "22"}

    while not answer_correct:
        answer_pl = input("Укажите две цифры номер строи и столбца для | " + X2 +" | в формате 00: ")
        a_empty = str("-")
        inv_answer_base = {value: key for key, value in answer_base.items()}
        try:
            if answer_pl in answer_base.values():
                answer_pl_write = pole[inv_answer_base.get(answer_pl)]
                print(answer_pl_write)
                if answer_pl_write is a_empty:
                    pole[inv_answer_base.get(answer_pl)] = X2
                    answer_correct = True
                else:
                    print("Занято тут")

        except:
            print("Некорректный ответ, ответ должен быть в виде 00 01 02 и т.д.: ")
            continue


def checkpole():
    # проверка на победителя
    checklist = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for check in checklist:
        if pole[check[0]] == pole[check[1]] == pole[check[2]] == "X":
            print("X победил ")
            return True
    for check in checklist:
        if pole[check[0]] == pole[check[1]] == pole[check[2]] == "O":
            print("O победил")
            return True
    # перебираем на поиск оставшихся свободных ячеек
    for i in range(8):
        if pole[i] == "-":
            return False
    # ходов больше нет - конец игры
    print("Ничья")
    return True

endGame = False
while not endGame:
    answer(X2)
    if X2 == "X":
        X2 = "O"
    else:
        X2 = "X"
    drawpole2(pole)
    endGame = checkpole()
