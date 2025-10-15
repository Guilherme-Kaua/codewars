def likes(names):
    #Duas variaveis para não repetir muito código
    one = " likes this"
    twoormore = " like this"

    #Se nulo, ninguém gosta
    if names == []:
        return "no one" + one
    #apenas 1
    elif len(names) == 1:
        return names[0] + one
    #apenas 2
    elif len(names) == 2:
        return names[0] + " and " + names[1] + twoormore
    #apenas 3
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + twoormore
    #mais que 3
    else:
        #fiz uma subtração entre o tamanho da lista menos 2, porque, o enunciado pedia para aqueles
        #maiores que 3, mostrar os dois primeiros indices e o resto apenas contar
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others" + twoormore
     