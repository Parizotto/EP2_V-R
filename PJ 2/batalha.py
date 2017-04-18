PERDEU = 0
VENCEU = 1
import random
import time, sys
import json
def batalha(player, inimigo):
	with open("database.json") as arquivo:
		dados = json.load(arquivo)
	fugir_lento = [1,2,3,4,5,6,7,8,9,10]
	fugir_rapido = [1,2,3,4,5]
	run= ("Fugiu")
	database = dados["database"]
	player = dados["player"]
	while True:
		resposta = input("\nvocê deseja:\n1 - fugir\n    ou\n2 - batalhar\n")
		conseguiu = ("\nsucesso na fuga\n")
		nao_conseguiu =("\nNão conseguiu fugir\nBatalhando em:\n3\n2\n1\n")
		batalhando= ("batalhando em:")
		numeros =("\n3\n2\n1\n")
		if resposta == "1":
			if (player["poder"]) >= (inimigo["poder"]):
				run_fast = fugir_rapido[random.randrange(len(fugir_rapido))]
				if run_fast == 1 or run_fast == 3 or run_fast == 5:
					for character in conseguiu:
						sys.stdout.write(character)
						sys.stdout.flush()
						time.sleep(0.1)
					break
				else:
					for character in nao_conseguiu:
						sys.stdout.write(character)
						sys.stdout.flush()
						time.sleep(0.1)
					while player["vida"]>0 and inimigo["vida"]>0:
						inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
						player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
						print("a vida do seu pokemon: {0}".format(player["vida"]))
						if inimigo["vida"]<=0:
							return VENCEU
							break
						if player["vida"] <=0:
							return PERDEU
							break
			if (player["poder"]) <= (inimigo["poder"]):
				run_slow = fugir_lento[random.randrange(len(fugir_lento))]
				if run_slow == 3 or run_slow == 8 or run_slow == 5:
					for character in conseguiu:
						sys.stdout.write(character)
						sys.stdout.flush()
						time.sleep(0.1)
					break
				else:
					for character in nao_conseguiu:
						sys.stdout.write(character)
						sys.stdout.flush()
						time.sleep(0.1)
					while player["vida"]>0 and inimigo["vida"]>0:
						inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
						player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
						print("a vida do seu pokemon: {0}".format(player["vida"]))
						if inimigo["vida"]<=0:
							return VENCEU
							break
						if player["vida"] <=0:
							return PERDEU
							break
		if resposta == "2":
			for character in batalhando:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.1)
			for character in numeros:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.2)
			while player["vida"]>0 and inimigo["vida"]>0:
				inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
				player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
				print("a vida do seu pokemon: {0}".format(player["vida"]))
			if inimigo["vida"]<=0 :
				return VENCEU
				break
			if player["vida"] <=0:
				return PERDEU
				break
		else:
			print("nao existe")