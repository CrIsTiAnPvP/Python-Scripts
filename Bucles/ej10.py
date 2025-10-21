n = int(input("Introduce un número entero: "))
is_prime = n > 1 and not any(n % i == 0 for i in range(2, int(n**0.5) + 1))

print("Es primo" if is_prime else "No es primo1")