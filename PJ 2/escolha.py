PASSEAR = 0
DORMIR = 1
import time, sys
def escolha():
	while True:
		hue = "vamos la.....\o/\n"
		resposta = input("Você deseja passear ou dormir?")
		if resposta == "passear":
			for character in hue:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			return PASSEAR
		if resposta == "dormir":
			print("okay")
			return DORMIR
		else:
			print("nao existe")
