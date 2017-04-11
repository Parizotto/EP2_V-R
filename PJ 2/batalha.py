PERDEU = 0
VENCEU = 1
import random
def batalha(player, inimigo):
	fugir_lento = [1,2,3,4,5,6,7,8,9,10]
	fugir_rapido = [1,2,3,4,5]
	run= ("Fugiu")
	resposta = int(input("\nvocê deseja:\n1 - fugir\n   ou\n2 - batalhar\n"))	
	while True:
		conseguiu = ("\nsucesso na fuga\n")
		if resposta == 1: #se quiser fugir ele vai rodar as opçoes
			if (player["poder"]) >= (inimigo["poder"]): #chance alta de fugir
				run_fast = fugir_rapido[random.randrange(len(fugir_rapido))]
				if run_fast == 1 or run_fast ==3 or run_fast == 5:
					print("Fugiu")
					break
				else:
					print("\nVocê não pode fugir\n")
					while player["vida"]>0 and inimigo["vida"]>0:
						inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
						player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
						if inimigo["vida"]<=0:
							return VENCEU
							break
						if player["vida"] <=0:
							return PERDEU
							break
			if (player["poder"]) <= (inimigo["poder"]):
				run_slow = fugir_lento[random.randrange(len(fugir_lento))]
				if run_slow == 3 or run_slow ==8 or run_slow == 5:
					print("Fugiu")
					break
				else:
					print("\nVocê não pode fugir\n")
					while player["vida"]>0 and inimigo["vida"]>0:
						inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
						player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
						if inimigo["vida"]<=0:
							return VENCEU
							break
						if player["vida"] <=0:
							return PERDEU
							break
		if resposta == 2:
			while player["vida"]>0 and inimigo["vida"]>0:
				inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
				player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
			if inimigo["vida"]<=0 :
				return VENCEU
				break
			if player["vida"] <=0:
				return PERDEU
				break


	# 	resposta= int(input('você quer fugir(1) ou batalhar(2)'))
	# 	if resposta == 1:
	#              if (inimigo['poder']) >= (player['poder']):
	#                       print("Você não pode fugir")
	# 	       continue
	# 	if resposta == 2:
	#               while player["vida"]>0 and inimigo["vida"]>0:
	#	                inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
	#	                player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
	#               if  inimigo["vida"]<=0 :
	#	                return VENCEU
	#               if player["vida"] <=0:
	#	                return PERDEU
	# 		
	# 	
	# 	else:
	# 		print('nao existe essa opção')
	# 		continue
