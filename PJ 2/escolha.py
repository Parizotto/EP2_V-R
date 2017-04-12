<<<<<<< HEAD
import time, sys, json

<<<<<<< HEAD
PASSEAR = 0
DORMIR = 1
MEU_POKEMON = 2
POKEDEX = 3
 
def escolha():
=======
def escolha(insperdex):

	with open("database.json") as arquivo:
		dados = json.load(arquivo)

	database = dados["database"]

	player = dados["player"]

>>>>>>> origin/master
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
			return MEU_POKEMON

		if resposta == "pokedex" or resposta == "4":
<<<<<<< HEAD
			return POKEDEX
=======
			print("\nvocê já avistou os pokemons:")
			for ind in range(len(insperdex)):
				print(insperdex[ind])

>>>>>>> origin/master

		else:
			print("nao existe")
=======
import time, sys, json

<<<<<<< HEAD
PASSEAR = 0
DORMIR = 1
MEU_POKEMON = 2
POKEDEX = 3
 
def escolha():
=======
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
			return MEU_POKEMON

		if resposta == "pokedex" or resposta == "4":
			return POKEDEX
			print("\nvocê já avistou os pokemons:")
			for ind in range(len(insperdex)):
				print(insperdex[ind])
		else:
			print("nao existe")
>>>>>>> 793d65523394b27c1967480205bfbd7d52f2eb41
