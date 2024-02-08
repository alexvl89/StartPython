def calcCountWordsAndChars(s: str) -> tuple[int, int]:
    """
    Возвращает количество слов и количество символов в строке без учета пробелов.

    :param s: Входная строка.
    :return: Кортеж, содержащий количество слов и количество символов без учета пробелов.
    """
    # разделеям на список и считаем количество элементов
    word_count = len(s.split())

    # убираем пробелы в строке
    char_count = len(s.replace(' ', ''))
    return word_count, char_count


# Пример использования:
S = "Привет, как дела, дружище?"
wordCount, charCount = calcCountWordsAndChars(S)
print(f"Количество слов: {wordCount}")
print(f"Количество символов без учета пробелов: {charCount}")
