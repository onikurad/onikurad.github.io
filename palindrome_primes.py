def is_prime(x):
    prime = True
    n = 1
    if x == 1:
        return False
    while n in range(1, x): 
        if x % n == 0 and n > 1 and n < x: 
            prime = False
            break
        n += 1
    return prime

def pal(x):
    num = x
    pal = 0
    while num != 0:
        digit = num % 10
        pal = pal * 10 + digit
        num //= 10

    return pal

def pal_prime(x, y):
    primes_list = []
    while x <= y:
        if x == pal(x) and is_prime(x) == True: 
            primes_list.append(x)
        x += 1
    return primes_list

print(pal_prime(10000, 99999))
