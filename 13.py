def eh_primo(num):
    if num == 2:
        return True
    if num < 2:
        return False
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True

a = list()
for i in range(50000):
    if eh_primo(i):
        a.append(i)

print(a[1335])
print(a[1336])
print(a[1337])