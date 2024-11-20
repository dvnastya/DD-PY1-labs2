salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_spend = 0  # Общие расходы
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for month in range(1, months + 1):  # 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10
    total_spend += spend
    spend_1 = spend * increase  # Увелечение трат
    spend = spend + spend_1
money_capital = total_spend - (salary * months)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
