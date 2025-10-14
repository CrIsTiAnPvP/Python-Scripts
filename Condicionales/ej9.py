e = int(input("Introduce tu edad: "))

match e:
	case e if e < 4:
		print("Puedes entrar gratis!")
	case e if e > 4 and e <= 18:
		print("Debes pagar 5€")
	case _:
		print("Debes pagar 10€")