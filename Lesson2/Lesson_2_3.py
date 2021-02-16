"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict."""

month_dict = {
    "Зима": [1, 2, 12],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11]
}

while True:
    try:
        month_number = int(input("Введите номер месяца (1-12): "))
        if 12 >= month_number >= 1:
            for key, value in month_dict.items():
                if month_number in value:
                    print(f"Время года:  {key}")
            break
    except ValueError:
        print("Введите корректное значение")
