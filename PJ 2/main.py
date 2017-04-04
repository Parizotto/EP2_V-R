import json
import random

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
	if resposta == DORMIR:
		break
	elif resposta == PASSEAR:
		# Vai rolar batalha.
		inimigo = escolher(database)

		print("Nome = {0}".format(inimigo["nome"]))
		print("Poder = {0}".format(inimigo['poder']))
		print("Vida = {0}".format(inimigo["vida"]))
		print("Defesa = {0}".format(inimigo["defesa"]))

		resultado = batalha(player, inimigo)
		if resultado == PERDEU:
			print("perdeu")
		elif resultado == VENCEU:
			print("venceu")





