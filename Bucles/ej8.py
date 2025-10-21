n = int(input("Introduce un número entero: "))

for i in range(1, n + 1):
	print(" ".join(str(k) for k in range(2 * i - 1, 0, -2)))