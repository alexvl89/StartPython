# выполняем импорт значения PI с библиотеки math
from math import pi


class PiNum:
    """ Класс хранения числа pi

    Returns:
        _type_: Позволяет вернуть число pi с заданной точностью
    """
    maxPi = pi

    def __init__(self, prec=2):
        """Инициализация

        Args:
            prec (int, optional): _description_. Defaults to 2.
        """
        self.set_pi_prec(prec)

    def set_pi_prec(self, prec):
        """Выполняем округление числа pi с заданной точностью prec

        Args:
            prec (_type_): _description_
        """
        self.currentPi = round(self.maxPi, prec)

    def __str__(self):
        return str(self.currentPi)


# Создаем экземпляр класса PiNum с точностью в три знака после запятой 3.142
piInstance = PiNum(3)
print(piInstance)

# Изменяем точность представления числа до пяти знаков после запятой 3.14159
piInstance.set_pi_prec(5)
print(piInstance)

# Выводим на экран значение числа Пи с максимальной точностью 3.141592653589793
print(PiNum.maxPi)
