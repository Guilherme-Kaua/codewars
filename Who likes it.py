def likes(names):
    #Se nulo, ninguém gosta
    if names == []:
        return "no one likes this"
    #apenas 1
    elif len(names) == 1:
        return (f"{names[0]} likes this")
    #apenas 2
    elif len(names) == 2:
        return (f"{names[0]} and {names[1]} like this")
    #apenas 3
    elif len(names) == 3:
        return (f"{names[0]}, {names[1]} and {names[2]} like this")
    #mais que 3
    else:
        #fiz uma subtração entre o tamanho da lista menos 2, porque, o enunciado pedia para aqueles
        #maiores que 3, mostrar os dois primeiros indices e o resto apenas contar
        return (f"{names[0]}, {names[1]} and {(len(names) - 2)} others like this")
     