"""6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
"""

analytics = {}
goods_list = []
count = 1

# наполнение структуры данных "Товары"
while True:
    print("Введите характеристики товара")
    features_dict = {"Название": "", "Цена": "", "Количество": "", "Единица измерения": ""}
    for feature in features_dict.keys():
        while True:
            user_value = input(f"{feature}: ")
            if len(user_value) != 0:
                break
            else:
                print("Введите корректное значение")
        features_dict[feature] = user_value
    goods_list.append(tuple([count, features_dict]))
    count += 1
    user_choice = input("Чтобы продолжить вносить товары нажмите Enter, для расчета аналитики введите w, "
                        "для выхода - q ").lower()
    if user_choice == "w":
        break
    elif user_choice == "q":
        exit(0)

print(goods_list)

# расчет аналитики
for good in goods_list:
    for key, value in good[1].items():
        if key in analytics:
            # заносим только уникальные значения
            if value not in analytics[key]:
                analytics[key].append(value)
        else:
            analytics[key] = [value]

print(f"Аналитика Ваших товаров: {analytics}")
