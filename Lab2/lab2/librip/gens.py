import random

# Генератор вычленения полей из массива словарей
def field(arr, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    for el in arr:  # где el - словарь
        slovar = {}
        for arg in args:
            if (arg in el.keys()) and (len(args) == 1):
                yield el[arg]  # генератор выдает только значения полей
            elif arg in el is not None:
                slovar[arg] = el[arg]  # формируем новый словарь,
                # где пропускаем элементы равные None
        if len(slovar) > 0 and len(args) > 1:
            yield slovar


# Генератор списка случайных чисел
def gen_random(begin, end, num_count):
    # Необходимо реализовать генератор
    for i in range(num_count):
        yield random.randint(begin, end)