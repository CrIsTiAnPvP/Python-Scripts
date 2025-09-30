pes=input('Dime tu peso corporal (en Kg): ')
alt=input('Dime tu altura (en cm): ')

res = float(pes) / ((float(alt) / 100) ** 2)

print(f'Tu IMC es de: {res}')