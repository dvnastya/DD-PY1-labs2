money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    month += 1
    if spend <= money_capital + salary:
        money_capital = money_capital + salary - spend
        spend_1 = spend * increase  # Увелечение трат
        spend = spend + spend_1
    else:
        month -= 1  # Убираем месяц, в который появилисся долг
        break
print("Количество месяцев, которое можно протянуть без долгов:", month)
