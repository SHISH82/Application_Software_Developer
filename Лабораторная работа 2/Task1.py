money_capital = 20000 salary = 5000spend = 6000 increase = 0.05 months = 0capital_per_months = money_capital + salarymonths_spend = spendwhile capital_per_months >= months_spend: months += 1 capital_per_months -= months_spend capital_per_months+= salary months_spend *= (1 + increase)print("Количество месяцев, которое можно протянуть без долгов:", months)