
number = [int(x) for x in range(1000)]
print(number)

for i in number:
    if i % 7 == 0 and i % 10 == 7:
        print(i)