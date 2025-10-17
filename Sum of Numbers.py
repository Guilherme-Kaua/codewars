def get_sum(a,b):
    

    soma = 0
    if a == b:
        return a

    if a < b:
        for i in range(a,b + 1):
            soma += i
    elif b < a:
        for i in range(b, a + 1):
            soma += i
    return soma


print(get_sum(0,-1))