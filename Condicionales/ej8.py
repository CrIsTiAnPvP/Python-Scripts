p, n, c = float(input("Introduce tu puntuación: ")), None, 2400
if p == 0.0:
	n, c = "Inaceptable", c * p
elif p == 0.4:
	n, c = "Aceptable", c * p
elif p >= 0.6:
	n, c = "Meritorio", c * p