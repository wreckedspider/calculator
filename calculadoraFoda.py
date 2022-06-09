modulo = input('Olá, usuário, qual o tipo de conta que você deseja fazer? (digite as três primeiras letras da operação básica que você deseja) ')
if modulo == "som":
	numberOne = int(input('Qual o primeiro termo da sua soma? '))
	numberTwo = int(input('Qual o segundo termo da sua soma? '))
	result = numberOne + numberTwo
	print(str(result))

elif modulo == 'sub':
	numberOne = int(input('Qual o primeiro termo da sua subtração?'))
	numberTwo = int(input('Qual o segundo termo da sua subtração?'))
	result = numberOne - numberTwo
	print(str(result))

elif modulo == 'mul':
	numberOne = int(input('Qual o primeiro termo da sua multiplicação?'))
	numberTwo = int(input('Qual o segundo termo da sua multilicação?'))
	result = numberOne * numberTwo
	print(str(result))

elif modulo == 'div':
	numberOne = int(input("Qual o número que você deseja dividir?"))
	numberTwo = int(input("Qual o número que você deseja usar como divisor?"))
	result = numberOne / numberTwo
	print(str(result))
