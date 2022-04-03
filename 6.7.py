n = int(input("Please type in a number:"))

def fib(n): 
    i=0
    if n<2:
        return(1)
    else:
        f=[0]*n 
        f[0]=1
        f[1]=1
        for i in range(2,n):
            f[i]=f[i-1]+f[i-2]
    return(f[i])

def big_fibonacci(n):
    count='1'
    num=1
    while(len(count)<n):
        count=str(fib(num))
        num+=1
    return(count)

print(big_fibonacci(n))
