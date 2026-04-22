from functools import reduce

numbers = [1, 2, 3, 4, 5]

# MAP: Применяет функцию к каждому элементу (делаем квадраты)
squares = list(map(lambda x: x**2, numbers)) 
# Результат: [1, 4, 9, 16, 25]

# FILTER: Оставляет только те элементы, которые прошли условие (только четные)
evens = list(filter(lambda x: x % 2 == 0, numbers)) 
# Результат: [2, 4]

# REDUCE: Сводит весь список к одному значению (считаем сумму)
total_sum = reduce(lambda x, y: x + y, numbers) 
# Результат: 15