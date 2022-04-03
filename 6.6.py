list = [1, 2, 3, 4, 5]
my_reverse = len(list)

for i in range(int(my_reverse / 2)):
    n = list[i]
    list[i] = list[my_reverse - i - 1]
    list[my_reverse - i - 1] = n

print(list)
