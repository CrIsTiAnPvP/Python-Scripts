i_an = 0.04
cant = int(input("Ingrese la cantidad en tu cuenta (€): "))

def calc_int(cant: int, interes: float, años: int) -> float:
	return cant * interes * años

print(f"El interés generado en un año es: {(cant + calc_int(cant, i_an, 1)):.2f}€")
print(f"El interés generado en dos años es: {(cant + calc_int(cant, i_an, 2)):.2f}€")
print(f"El interés generado en tres años es: {(cant + calc_int(cant, i_an, 3)):.2f}€")