money_capital = 20000 # Подушка безопасности
salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
increase = 0.05 # Ежемесячный рост цен
months = 0

capital_per_months = money_capital + salary
months_spend = spend

while capital_per_months >= months_spend:
 months += 1
 capital_per_months -= months_spend
 capital_per_months+= salary
 months_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)


