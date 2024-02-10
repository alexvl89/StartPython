class Employee:
    """Работник
    """

    def __init__(self, name, position=None, salary=0):
        """Инициализация

        Args:
            name (_type_): Имя
            position (_type_, optional): должность . Defaults to None.
            salary (int, optional): зарплата. Defaults to 0.
        """
        self.name = name
        self.position = position
        self.salary = salary

    def increaseSalary(self, portion):
        """Увеличение оклада на portion процентов с округлением до копеек

        Args:
            portion (_type_): процент для увеличения
        """
        self.salary = round(self.salary * (1 + portion), 2)

    def __str__(self):
        """Переопределение вывода в строке

        Returns:
            _type_: _description_
        """
        return f"Имя: {self.name}\nДолжность: {self.position}\nЗарплата: {self.salary}\n"


class Manager(Employee):
    """ Менеджер унаследованный от работника

    Args:
        Employee (_type_): Работник
    """

    def increaseSalary(self, portion, bonus):
        """Переопределение повышения зарплаты

        Args:
            portion (_type_): процент увеличения
            bonus (_type_): дополнительный бонус
        """
        self.salary = round(self.salary * (1 + portion + bonus), 2)


# Выполнение примера
ivanManager = Manager("Иван", position="Менеджер", salary=1700)
print(ivanManager)
ivanManager.increaseSalary(0.335, 0.25)
print(ivanManager)
