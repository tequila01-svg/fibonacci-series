def fibonacci_series(n):
    
    a,b = 0,1
    series=[]
    
    for _ in range(n):
        series.append(a)
        a,b = b, a+b
        
    return series

n = int(input("enter the number of terms for the fibonacci series:"))

if n<=0:
    print("please enter a positive integer.")
else:
    fib_series = fibonacci_series(n)
    print("fibonacci series:", fib_series)
    