n, a = int(input("Introduce un número positivo: ")), []
for i in range(1, n+1):
	if i % 2 != 0:
		a.append(str(i))
print(", ".join(a))