"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

numbers_list = [x for x in range(20, 241) if (x % 20 == 0) or (x % 21 == 0)]
print("Числа, кратные 20 или 21 в пределах от 20 до 240:")
print(*numbers_list)
