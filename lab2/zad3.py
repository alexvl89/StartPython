def insertSeparator(s: str, sep: str) -> str:
    """
    Вставляет разделитель sep между символами строки s.

    :param s: Входная строка.
    :param sep: разделитель.
    :return: Новая строка с разделителем.
    """
    return sep.join(s)


s = "Привет"
separator = "*_"
result = insertSeparator(s, separator)
print(result)
