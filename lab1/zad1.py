# Ввод данных с клавиатуры
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Операции калькулятора
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Проверка деления на ноль
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Деление на ноль невозможно"

# Вывод результатов на экран
print("Сумма:", sum_result)
print("Разность:", difference_result)
print("Произведение:", product_result)
print("Частное:", division_result)
