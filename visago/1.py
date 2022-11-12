s = 0
n = int(input("> "))
while n >= 0:
    s += n
    if (s >= 100):
        s = 0
    n = int(input("> "))
print(n, s)