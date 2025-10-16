# A raiz numérica é a soma recursiva de todos os dígitos de um número.
# Dado n, calcule a soma dos dígitos de n. 
# Se esse valor tiver mais de um dígito, 
# continue reduzindo dessa forma até que um número de um dígito seja produzido. 
# A entrada será um número inteiro não negativo.

# Uma outra função para fazer recursividade em outra função, minimizando a funcionalidade de cada uma
def verifica_mais(n):
    variavel = 0
    if (len(n) >= 2):
        #faço a soma dos digitos
        for i in range(len(n)):
            variavel += int(n[i])

    n = str(variavel)

    if (len(n) >= 2):
        variavel = 0
        #faço a soma dos digitos mais uma vez
        for i in range(len(n)):
            variavel += int(n[i])  
        return variavel
    else:
        return variavel


def digital_root(n):
    n = str(n)
    soma = 0
    #faço a soma dos digitos
    for i in range(len(n)):
        soma += int(n[i])

    n = str(soma)

    if (len(n) >= 2):
        #verifico a soma dos digitos mais uma vez, só que agora em outra função
        return verifica_mais(n)
    else:
        #se não tiver mais que 2 digitos, apenas retorne 
        return int(n)
