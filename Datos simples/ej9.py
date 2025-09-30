def calcular_interes(capital: float, interes: float, tiempo: float) -> float:
        return capital * interes * tiempo

c = float(input("Introduce el capital inicial (en €): "))
i = float(input("Introduce el interés anual (en %): "))
t = float(input("Introduce el tiempo (en años): "))

inter_gen = calcular_interes(c,i/100,t)

print (f"El interés generado es: {inter_gen:.2f} € ({inter_gen + c:.2f}€)")