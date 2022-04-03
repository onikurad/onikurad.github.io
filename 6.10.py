n = int(input("Enter a number: "))

for x in range (2, n+1):
    is_prime = True
    for y in range (2, x):
        if x % y == 0:
            is_prime= False   

    if is_prime:
        print (x)
