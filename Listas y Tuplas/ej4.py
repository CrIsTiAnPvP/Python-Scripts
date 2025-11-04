n, fin = [], False
while (not fin):
	num = input('Introduce un número de la primitiva: ')

	if len(num) < 2 and int(num) < 10: num = '0' + num
	elif len(num) > 2: print('Número incorrecto. Debe tener 1 o 2 dígitos.'); continue
	elif num in n: print('Número repetido. Introduce otro número.'); continue
	
	n.append(num)
	if len(n) == 8: n.sort(); fin = True

print(" ".join(n))