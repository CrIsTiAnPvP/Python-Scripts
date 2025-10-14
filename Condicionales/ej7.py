r = float(input("Introduce tu renta anual (€): ")); print("Tipo impositivo de: ", end="")
match r:
	case r if r < 10000: print("5%")
	case r if r < 20000: print("15%")
	case r if r < 35000: print("20%")
	case r if r < 60000: print("30%")
	case _: print("45%")