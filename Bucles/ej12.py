f, l, c = input("Introduce una frase: "), input("Introduce una letra: "), 0

for i in f:
	if i.lower() == l.lower(): c+=1
print(f"La letra {l} aparece {c} {"vez" if c < 2 else "veces"}")