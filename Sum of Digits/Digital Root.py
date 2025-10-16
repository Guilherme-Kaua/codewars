# A raiz numérica é a soma recursiva de todos os dígitos de um número.
# Dado n, calcule a soma dos dígitos de n. 
# Se esse valor tiver mais de um dígito, 
# continue reduzindo dessa forma até que um número de um dígito seja produzido. 
# A entrada será um número inteiro não negativo.

def digital_root(n):
    while n >= 10:
        soma = 0
        for i in str(n):
            soma += int(i)
        n = soma
    if n < 10:
        return n   
