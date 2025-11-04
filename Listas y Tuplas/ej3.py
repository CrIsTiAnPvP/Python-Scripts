asignaturas, notas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"], []
for a in asignaturas:
	n = input(f'¿Que has sacado en {a}? '); notas.append(float(n))
print()
for i in range(len(asignaturas)): print(f'En {asignaturas[i]} has sacado {notas[i]}')