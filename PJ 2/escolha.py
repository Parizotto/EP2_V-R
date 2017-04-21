import time, sys, json
PASSEAR = 0
DORMIR = 1
MEU_POKEMON = 2
POKEDEX = 3
CARREGAR = 5
def escolha(insperdex):
	with open("database.json") as arquivo:
		dados = json.load(arquivo)
	database = dados["database"]
	player = dados["player"]
	while True:
		hue = "caminhando...\ncaminhando...\n"
		resposta = input("\nVocê deseja:\n\n 1 - passear\n 2 - dormir\n 3 - meu pokemon\n 4 - pokedex\n 5 - carregar jogo anterior\n\n")
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
			return MEU_POKEMON
		if resposta == "pokedex" or resposta == "4":
			return POKEDEX
		if resposta == "5":
			return CARREGAR
		else:
			print("nao existe")
