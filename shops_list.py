from numpy import np
from collections import Counter

# Функция для сплющивания списка
def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(item)
        else:
            flat.append(item)
    return flat

# Создаем счетчики для магазинов
center_list = Counter(flatten(center))
south_list = Counter(flatten(south))
north_list = Counter(flatten(north))



