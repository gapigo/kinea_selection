def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# for i in range(1, 10):
#    print(fib(i), end=' ')
# print(fib(1))
# print(fib(3))
print(fib(10))