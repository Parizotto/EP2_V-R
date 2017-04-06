PASSEAR = 0
DORMIR = 1
import time, sys, json, 

def escolha():

	with open("database.json") as arquivo:
		dados = json.load(arquivo)

	database = dados["database"]

	player = dados["player"]

	while True:
		hue = "vamos la.....\o/\n"
		resposta = input("Você deseja:\n passear(1)?\n dormir(2)?\n ver o meu pokemom(3)?\n pokedex(4)\n")

		if resposta == "passear" or resposta == "1":
			for character in hue:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			return PASSEAR

		if resposta == "dormir" or resposta == "2":
			print("okay")
			return DORMIR

		if resposta == "ver o meu pokemom" or resposta == "3":
			print("Nome = {0}".format(player["nome"]))
			print("Poder = {0}".format(player['poder']))
			print("Vida = {0}".format(player["vida"]))
			print("Defesa = {0}".format(player["defesa"]))
			break

		if resposta == "pokedex" or resposta == "4":
			pass


		else:
			print("nao existe")
