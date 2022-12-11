spend = 6000  # траты
salary = 5000  # зарплата
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
delta = 0  # нехватка средств к существованию

while months > 0:  # рассчет подушки

    delta = spend - salary
    need_money += delta
    spend = spend * increase + spend
    months -= 1

print(round(need_money))
