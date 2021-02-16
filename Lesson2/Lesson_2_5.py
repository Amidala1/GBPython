"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них."""

rating_list = [7, 5, 3, 3, 2]
new_rate = None

while True:
    while True:
        try:
            new_rate = input("Введите натуральное число либо q для выхода из программы: ").lower()
            if new_rate == "q":
                print("Вы вышли из программы")
                exit(0)
            elif int(new_rate) <= 0:
                print("Введите корректное значение")
            else:
                new_rate = int(new_rate)
                break
        except ValueError:
            print("Введите корректное значение")
    count = rating_list.count(new_rate)
    if count > 0:
        rate_index = rating_list.index(new_rate)
        rating_list.insert(rate_index + count, new_rate)
    else:
        rating_list.append(new_rate)
        rating_list.sort(reverse=True)
    print(f"Рейтинг: {rating_list}")

