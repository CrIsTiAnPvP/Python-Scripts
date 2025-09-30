n = int(input('Introduce un número entero: '))
m = int(input('Introduce otro número entero: '))

res = n / m 
coc = n // m
resto = n % m

print(f'El resultado de {n} entre {m} es {res}, el cociente es {coc} y el resto es {resto}.')