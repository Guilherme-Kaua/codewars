lista = []

def solution(n):
    soma = 0
    if n <= 0:
        return 0
    for i in range(2,n):
        if i % 3 == 0 or i % 5 == 0 :
            soma+= i

    return soma


