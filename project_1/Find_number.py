import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
        
    # ключевое отличие в сужение диапазонов поиска числа за счет уменьшения границ
    """
    count = 0
    a = 1
    b = 101
    predict = np.random.randint(a, b)

    while number != predict:
        count += 1
        if number > predict:
          a = predict
          predict = np.random.randint(a, b)
        elif number < predict:
          b = predict + 1
          predict = np.random.randint(a, b)

    return count