PASSEAR = 0
DORMIR = 1
<<<<<<< HEAD
import time, sys, json
=======
import time, sys, json 
>>>>>>> 73ae7e21a238a413edeb89c5299f4b97ef24d2b0

def escolha():

	with open("database.json") as arquivo:
		dados = json.load(arquivo)

	database = dados["database"]

	player = dados["player"]

	while True:
		hue = "vamos la.....\o/\n"
		resposta = input("Você deseja:\n\n 1 - passear?\n 2 - dormir?\n 3 - meu pokemom?\n 4 - pokedex\n\n")

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
			print("você encontrou um pokemom! \n")
			print("Nome = {0}".format(player["nome"]))
			print("Poder = {0}".format(player['poder']))
			print("Vida = {0}".format(player["vida"]))
			print("Defesa = {0}".format(player["defesa"]))
			break

		if resposta == "pokedex" or resposta == "4":
			pass


		else:
			print("nao existe")
