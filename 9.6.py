def all_variants(text):
    """
    Функция-генератор, которая возвращает все подпоследовательности строки text.

    :param text: str - входная строка
    :yield: str - очередная подпоследовательность
    """
    for start in range(len(text)):  # Определяем начальный индекс
        for end in range(start + 1, len(text) + 1):  # Определяем конечный индекс
            yield text[start:end]  # Возвращаем срез строки
# Пример использования
a = all_variants("GDP")
for i in a:
    print(i)
