money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital > 0:
    money_capital = money_capital - spend + salary
    spend = spend * increase + spend
    month += 1

print(month - 1)  # так как первый месяц зафиксирован 0 и он уже был прожит ранее,
# то количество месяцев, прожитых по условию равно 5
