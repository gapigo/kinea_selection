def segredo(a):
    return ord(a)
T= lambda s: sum(map(segredo, s))
print(T("uma frase muito especial"))
print(T("esta frase eh muito grande pra calcular na mao"))