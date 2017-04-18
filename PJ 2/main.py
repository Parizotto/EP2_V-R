import json
import random
import time, sys

from escolha import *
from batalha import batalha, PERDEU, VENCEU

def escolher (database):
	inimigo = database[random.randrange(len(database))]
	return inimigo

with open("database.json") as arquivo:
    dados = json.load(arquivo)

database = dados["database"]
player = dados["player"]
insperdex = []
while True:

	resposta = escolha(insperdex)

	encontrou = ("\nvocê encontrou um pokemon:\n\n")
	win= ("\nseu pokemon ganhou! \o/\n")
	lose= ("\nvocê perdeu :(\n")
	if resposta == DORMIR:
		break
	elif resposta == PASSEAR:
		# Vai rolar batalha.
		inimigo = escolher(database)

		for character in encontrou:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.1)
		
		print("Nome = {0}".format(inimigo["nome"]))
		print("Poder = {0}".format(inimigo['poder']))
		print("Vida = {0}".format(inimigo["vida"]))
		print("Defesa = {0}".format(inimigo["defesa"]))

		print("XP do seu pokemon = {0}".format(player["XP"]))


		if inimigo["nome"] not in insperdex:
			insperdex.append(inimigo["nome"])

		resultado = batalha(player,inimigo)
		
		if resultado == PERDEU:
			player["XP"]+=(inimigo["defesa"]+inimigo["poder"])//5
			for character in lose:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)
		elif resultado == VENCEU:
			player["XP"]+=(inimigo["defesa"]+inimigo["poder"])//2
			for character in win:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)

		if player["XP"] >=10 :
			player["nome"]="raiochu"
			player["poder"]=53
			player["vida"]=190
			player["defesa"]=24


	elif resposta == MEU_POKEMON:
		print("Nome = {0}".format(player["nome"]))
		print("Poder = {0}".format(player['poder']))
		print("Vida = {0}".format(player["vida"]))
		print("Defesa = {0}".format(player["defesa"]))

	elif resposta == POKEDEX:
		print("\nvocê já avistou os pokemons:")
		for ind in range(len(insperdex)):
			print(insperdex[ind])

