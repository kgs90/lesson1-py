print("День недели:")
day = int(input())

if (day > 7 or day < 1):
    print("неправильный день недели.")
else:
    if (day > 5):
        print("Выходной день")
    else: print("Рабочий день")