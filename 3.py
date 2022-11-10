maior = 0
for i in range(1, 100001):
    passos = 0
    num = i
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        passos += 1
    #print(i)
    if passos > maior:
        maior = passos

print(f'Maior: {maior}')