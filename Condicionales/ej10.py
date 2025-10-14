tipo, v, nv, i = input("¿Quieres una pizza vegetariana? (si/no): "), ["Pimiento", "Tofu"], ["Peperoni", "Jamón", "Salmón"], ["Mozzarella", "Tomate"]

print("Ingredientes: ", end="")
if tipo.lower() == "si": print(", ".join(v))
else: print(" ".join(nv))

ingrediente = input("Introduce un ingrediente: ")
i.append(ingrediente)
if tipo.lower() == "si": 
	if not ingrediente.lower().capitalize() in v: print("Error, la pizza es vegetariana") 
	else: print(f"Pizza vegetariana, ingredientes: {", ".join(i)}")
else:
	if not ingrediente.lower().capitalize() in nv: print("Error, la pizza no es vegetariana")
	else: print(f"Pizza no vegetariana, ingredientes: {", ".join(i)}")