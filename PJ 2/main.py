import json
import random
import time, sys

from escolha import escolha, DORMIR, PASSEAR
from batalha import batalha, PERDEU, VENCEU

def escolher (database):
	inimigo = database[random.randrange(len(database))]
	return inimigo

with open("database.json") as arquivo:
    dados = json.load(arquivo)

database = dados["database"]
player = dados["player"]

while True:
	resposta = escolha()
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
		
		

		resultado = batalha(player,inimigo)
		
		if resultado == PERDEU:
			for character in lose:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)
		elif resultado == VENCEU:
			for character in win:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)





