from datetime import datetime

# Запрос информации у пользователя
name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваш город проживания: ")
country = input("Введите вашу страну проживания: ")
birth_year = input("Введите ваш год рождения: ")

current_year = datetime.now().year
if ((int(current_year)-int(birth_year)) != int(age)):
    output = f"Уважаемый, проверьте год рождения или возраст"
else:
    # Оформление вывода
    output = f"Уважаемый {name}! На сегодняшний день Вы проживаете в стране {country}, в городе {city}, и вы родились в {birth_year} году."

# Вывод результата
print(output)
