from json import *
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
ja_evoluiu = False
while True:
	resposta = escolha(insperdex)
	encontrou = ("\nvocê encontrou um pokemon:\n\n")
	win= ("\nseu pokemon ganhou! \o/\n")
	lose= ("\nvocê perdeu :(\n")
	evoluir= ("\nseu pokemon evoluiu  \o/")
	if resposta == DORMIR:
		break
	elif resposta == PASSEAR:
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
		if player["XP"] >=5 and not ja_evoluiu:
			for character in evoluir:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			player["nome"]="raichu"
			player["poder"]=53
			player["vida"]=190
			player["defesa"]=24
			ja_evoluiu = True
	elif resposta == MEU_POKEMON:
		print("Nome = {0}".format(player["nome"]))
		print("Poder = {0}".format(player['poder']))
		print("Vida = {0}".format(player["vida"]))
		print("Defesa = {0}".format(player["defesa"]))
		print("XP = {0}".format(player["XP"]))
	elif resposta == POKEDEX:
		print("\nvocê já avistou os pokemons:")
		for ind in range(len(insperdex)):
			print(insperdex[ind])
	elif resposta == CARREGAR:
		with open("insperdex_salvo.json","r") as file:
			insperdex = json.load(file)
		with open("evolucao_salvo.json","r") as hue:
			player = json.load(hue)
with open("insperdex_salvo.json","w") as file:
	json.dump(insperdex, file)
with open("evolucao_salvo.json","w") as hue:
	json.dump(player, hue)
