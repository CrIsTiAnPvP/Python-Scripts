c, i, n = int(input("Introduce una cantidad a invertir: ")), input("Introduce el porcentaje de interés anual: "), int(input("Introduce el número de años: "))

i = float(i.split("%")[0]) / 100

for an in range(1, n+1):
	c+=c*i
	print(f"Interés año {an} --> {c:.2f}")