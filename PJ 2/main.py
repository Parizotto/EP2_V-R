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
	#Frases auxiliares,algumas serão utilizadas com delay
	resposta = escolha(insperdex)
	encontrou = ("\nvocê encontrou um pokemon:\n\n")
	win= ("\nseu pokemon ganhou! \o/\n")
	lose= ("\nvocê perdeu :(\n")
	evoluir= ("\nseu pokemon evoluiu  \o/\n")
	if resposta == DORMIR:
		break
	#Caso escolha passear, o player podera ver o nome mais seus atributos do inpermon inimigo
	elif resposta == PASSEAR:
		inimigo = escolher(database)
		for character in encontrou:
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.1)
		print("     INIMIGO")
		print("Nome   = {0}".format(inimigo["nome"]))
		print("Poder  = {0}".format(inimigo['poder']))
		print("Vida   = {0}".format(inimigo["vida"]))
		print("Defesa = {0}".format(inimigo["defesa"]))
		print("\n\n VS\n\n")
		print("     PLAYER")
		print("Nome   = {0}".format(player["nome"]))
		print("Poder  = {0}".format(player['poder']))
		print("Vida   = {0}".format(player["vida"]))
		print("Defesa = {0}".format(player["defesa"]))
		print("XP     = {0}".format(player["XP"]))
		#If para checar se o inspermon ja esta em nosso pokedex
		if inimigo["nome"] not in insperdex:
			insperdex.append(inimigo["nome"])
		resultado = batalha(player,inimigo)
		if resultado == PERDEU:
			player["XP"]+=(-inimigo["defesa"]+inimigo["poder"])//5
			for character in lose:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)
		elif resultado == VENCEU:
			#Se o inpermom vencer, o ganho de xp é variavel e maior do quando perder
			player["XP"]+=(-inimigo["defesa"]+inimigo["poder"])//2
			for character in win:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)
		# If para comparar o atual XP com o minimo necessario para evoluir
		if player["XP"] >=15 and not ja_evoluiu:
			for character in evoluir:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			#evolução de meu inspermon
			player["nome"]="raichu"
			player["poder"]=35
			player["vida"]=115
			player["defesa"]=12
			#variaval booleana para apenas evoluir uma vez
			ja_evoluiu = True

	elif resposta == MEU_POKEMON:
		print("Nome = {0}".format(player["nome"]))
		print("Poder = {0}".format(player['poder']))
		print("Vida = {0}".format(player["vida"]))
		print("Defesa = {0}".format(player["defesa"]))
		print("XP = {0}".format(player["XP"]))

	elif resposta == POKEDEX:
		if len(insperdex) < 1:
			print ("\nVocê não avistou nenhum pokemon ainda\n")
		else:
			print("\nVocê já avistou os pokemons:\n")
			for ind in range(len(insperdex)):
				print(insperdex[ind])

	elif resposta == CARREGAR:
		with open("insperdex_salvo.json","r") as file:
			insperdex = json.load(file)
		with open("evolucao_salvo.json","r") as hue:
			player = json.load(hue)
		with open("palavra_evolucao.json","r") as yei:
			ja_evoluiu = json.load(yei)
with open("insperdex_salvo.json","w") as file:
	json.dump(insperdex, file)
with open("evolucao_salvo.json","w") as hue:
	json.dump(player, hue)
with open("palavra_evolucao.json","w") as yei:
	json.dump("True",yei)