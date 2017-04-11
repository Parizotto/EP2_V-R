PASSEAR = 0
DORMIR = 1
import time, sys, json

def escolha(insperdex):

	with open("database.json") as arquivo:
		dados = json.load(arquivo)

	database = dados["database"]

	player = dados["player"]

	while True:
		hue = "caminhando...\ncaminhando...\n"
		resposta = input("\nVocê deseja:\n\n 1 - passear\n 2 - dormir\n 3 - meu pokemon\n 4 - pokedex\n\n")

		if resposta == "passear" or resposta == "1":
			for character in hue:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)
			return PASSEAR

		if resposta == "dormir" or resposta == "2":
			print("okay")
			return DORMIR

		if resposta == "meu pokemon" or resposta == "3":
			print("Nome = {0}".format(player["nome"]))
			print("Poder = {0}".format(player['poder']))
			print("Vida = {0}".format(player["vida"]))
			print("Defesa = {0}".format(player["defesa"]))
			break

		if resposta == "pokedex" or resposta == "4":
			print("\nvocê já avistou os pokemons:")
			for ind in range(len(insperdex)):
				print(insperdex[ind])


		else:
			print("nao existe")
