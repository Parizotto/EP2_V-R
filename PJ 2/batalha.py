PERDEU = 0
VENCEU = 1

def batalha(player, inimigo):
        
        while True:
                resposta= input("você quer fugir(1) ou batalhar(2): ")
                if resposta == "fugir" or resposta == "1":
                        if (inimigo["poder"]) <= (player["poder"]):
                                print("hue")
                        else:
                                print("Você não pode fugir")
                                while player["vida"]>0 and inimigo["vida"]>0:
                                        inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
                                        player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
                                        if  inimigo["vida"]<=0 :
                                                return VENCEU
                                        if player["vida"] <=0:
                                                return PERDEU
                if resposta == "batalhar" or resposta == "2":
                                while player["vida"]>0 and inimigo["vida"]>0:
                                        inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
                                        player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
                                if  inimigo["vida"]<=0 :
                                        return VENCEU
                                if player["vida"] <=0:
                                        return PERDEU


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
