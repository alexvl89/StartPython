""" четный - even
    нечетный - odd
"""

from typing import List, Tuple


def splitNums(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Разбивает список чисел на четные и нечетные.

    Args:
        numbers (List[int]): Входной список

    Returns:
        Tuple[List[int], List[int]]: Кортеж с четными и нечетными списками
    """
    odd = []
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return odd, even


# Пример:
numbers = [1, 2, 3, 4, 5, 10, 11]
odd, even = splitNums(numbers)
print("Четные числа:", even)
print("Нечетные числа:", odd)
