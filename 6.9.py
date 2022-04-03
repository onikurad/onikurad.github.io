num = int(input("Enter a number: "))

is_prime = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = True
            break

if is_prime:
    print(num, "is not a prime number!")
else:
    print(num, "is a prime number!")
