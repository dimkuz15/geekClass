print("Введите доход за этот месяц:")
money = int(input())
print("Введите количество сотрудников:")
sotr = int(input())
zp = 1
zpob = 0
while zp-1<sotr:
    print("Введите зарплату сотрудника",zp,":")
    a = int(input())
    zpob = zpob+a
    zp = zp+1
if money>zpob:
    print("Все хорошо")
else:
    print("Дохода не хватает!")
    print("Нужно дополнительно", zpob-money,"руб.")
