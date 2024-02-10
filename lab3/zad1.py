class Soda:
    """Класс для определения газированной воды
    """

    def __init__(self, additive=None):
        """Инициализация

        Args:
            additive (_type_, optional): Указывает имеется ли добавка (опционально)
        """
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")


# Вывод: Обычная газировка
soda = Soda()
soda.show_my_drink()

# Вывод: Газировка и лимон
soda = Soda("лимон")
soda.show_my_drink()
