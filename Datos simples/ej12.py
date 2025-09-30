p_pan = 3.49
desc = 0.6

b_vend = int(input("Introduce el número de barras vendidas (que no sean del día): "))

def calc_precio(b_vend: int, p_pan: float, desc: float) -> float:
	return b_vend * (p_pan - (p_pan * desc))


print(f"El precio del pan es de: {p_pan}€")
print(f"El precio del pan con descuento es de: {(p_pan - (p_pan * desc)):.2f}€")
print(f"El precio total de las barras vendidas es de: {calc_precio(b_vend, p_pan, desc):.2f}€")