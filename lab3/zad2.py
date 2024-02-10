class TriangleChecker:
    """Класс для проверки формирования треугольника по трем отрезкам определенной длины
    """

    def __init__(self, a, b, c):
        """Инициализация трех отрезков

        Args:
            a (_type_): длина отрезка a
            b (_type_): длина отрезка b
            c (_type_): длина отрезка c
        """
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> bool:
        """Проверка формирования треугольника по сторонам

        Необходимым и достаточным условием существования треугольника является выполнение следующих неравенств:
        a+b>c, a+c>b, b+c>a, (a>0, b>0, c>0),
        
        Returns:
            bool: true or false
        """

        # проверка на число функцией isinstance(переменная, типы данных на которые проверять)
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float))):
            return "Нужно вводить только числа!"
        # если хотя бы одна длина меньше 0
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"
        # проверка возможности построить треугльник
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


# Вывод: Ура, можно построить треугольник!
check1 = TriangleChecker(3, 4, 5)
print(check1.is_triangle())

# Вывод: С отрицательными числами ничего не выйдет!
check2 = TriangleChecker(3, -4, 5)
print(check2.is_triangle())

# Вывод: Нужно вводить только числа!
check3 = TriangleChecker('a', 4, 5)
print(check3.is_triangle())

# Вывод: Жаль, но из этого треугольник не сделать.
check4 = TriangleChecker(1, 2, 10)
print(check4.is_triangle())
