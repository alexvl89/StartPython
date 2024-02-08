
def printLine(n: int):
    """Печатаем через умножение

    Args:
        n (int): число повторений
    """
    line = '-'*n
    print(line)


def printLineWithLoop(n: int):
    """Печатаем через цикл

    Args:
        n (int): число повторений
    """
    line = ''
    for _ in range(n):
        line += '_'
    print(line)


def isIntValue(value: str) -> tuple[bool, int]:
    """Проверка на число

    Args:
        value (str): Входная строка

    Returns:
        tuple[bool, int]: Вычисленное значение
    """
    try:
        n = int(value)
        return True, n
    except ValueError:
        return False, 0


"""долго выполняем
"""
while True:
    inputValue = input("Введите n (для выхода введите 'q'): ")

    if inputValue == 'q':
        break

    # проверяем на число
    isInt, n = isIntValue(inputValue)

    # если не число, то ошибка
    if not isInt:
        print("Ошибка: введите целое число.")
        continue

    # печатаем
    printLine(n)
