
import time, sys, json

<<<<<<< HEAD

=======
>>>>>>> f9232a9443f938df7b9dadcf76271a90cfea348d
PASSEAR = 0
DORMIR = 1
MEU_POKEMON = 2
POKEDEX = 3
<<<<<<< HEAD
 
def escolha():
=======
>>>>>>> f9232a9443f938df7b9dadcf76271a90cfea348d

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
<<<<<<< HEAD



		else:
			print("nao existe")
=======
		else:
			print("nao existe")

>>>>>>> f9232a9443f938df7b9dadcf76271a90cfea348d
