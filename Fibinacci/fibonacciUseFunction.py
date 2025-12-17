def fib2(n):
    result = []
    a,b = 0, 1
    while a < n:
        result.append(a)
        print(result)
        a,b = b, a+b
    return result
    

fib2(1000)
