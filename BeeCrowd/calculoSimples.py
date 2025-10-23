#O arquivo de entrada contém duas linhas de dados. 
#Em cada linha haverá 3 valores, 
#respectivamente dois inteiros e um valor com 2 casas decimais.

x = input()
y = input()
lista1 = x.split(" ")
lista2 = y.split(" ")

for i in range(0,6):
    soma1 = int(lista1[1]) * float(lista1[2])
    soma2 = int(lista2[1]) * float(lista2[2])
    total = soma1 + soma2

print(f"VALOR A PAGAR: R$ {total:.2f}")