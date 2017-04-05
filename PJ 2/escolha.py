PASSEAR = 0
DORMIR = 1

def escolha():
	while True:
		resposta = input("Você deseja passear ou dormir?")
		if resposta == "passear":
			print("vamos la..... \o/")
			return PASSEAR
		if resposta == "dormir":
			print("okay")
			return DORMIR
		else:
			print("nao existe")
