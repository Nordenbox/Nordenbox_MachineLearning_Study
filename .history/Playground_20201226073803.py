
number = [int(x) for x in range(1, 1000)]
game_number = int(input('不许说出来的数字是： '))

for i in number:
    if i % game_number == 0 or i % 10 == game_number:
        print(i)