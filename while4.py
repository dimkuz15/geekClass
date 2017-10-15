b = 1
c = 0
print("Сколько лайков у поста",b,":")
a = int(input())
c = c+a
while a>-1:
    b=b+1
    print("Сколько лайков у поста",b,":")
    a = int(input())
    c = c+a
print("Среднее количество лайков:",(c+1)/(b-1))
