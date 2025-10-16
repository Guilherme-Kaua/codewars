# A raiz numérica é a soma recursiva de todos os dígitos de um número.
# Dado n, calcule a soma dos dígitos de n. 
# Se esse valor tiver mais de um dígito, 
# continue reduzindo dessa forma até que um número de um dígito seja produzido. 
# A entrada será um número inteiro não negativo.

def digital_root(n):
    n = str(n)
    soma = 0

    while len(n) > 1:
        soma = 0
        for i in range(len(n)):
            soma += int(n[i])
        n = str(soma)   
    return soma    


print(digital_root(16)) # 1 + 6 = 7
print(digital_root(942)) # 9 + 4 + 2 = 15 -> 1 + 5 = 6
print(digital_root(132189)) # 1 + 3 + 2 + 1 + 8 + 9 = 24 -> 2 + 4 = 6
print(digital_root(493193)) # 4 + 9 + 3 + 1 + 9 + 3 = 29 -> 2 + 9 = 11 -> 1 + 1 = 2      