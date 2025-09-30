p_pay = 112
p_mu = 75

def c_peso(unidades: int, peso: int) -> int:
	return unidades * peso

p = int(input("Introduce el número de payasos: "))
m = int(input("Introduce el número de muñecas: "))

peso_total = c_peso(p,p_pay) + c_peso(m,p_mu)
print(f"El peso total del pedido es: {peso_total} g")