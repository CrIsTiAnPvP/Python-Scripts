c = input('Introduce tu correo electrónico: ')
if not '@' in c: print('El correo electrónico debe contener @')
else: print(c.split('@')[0]+'@ceu.es')