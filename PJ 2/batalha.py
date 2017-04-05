PERDEU = 0
VENCEU = 1

def batalha(player, inimigo):
	while player["vida"]>0 and inimigo["vida"]>0:
		inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
		player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
	if  inimigo["vida"]<=0 :
		return VENCEU
	if player["vida"] <=0:
		return PERDEU	
	# if (inimigo['poder']) >= (player['poder']):
	# 	FAZER A BATALHA
	# else:
	# 	resposta= int(input('você quer fugir(1) ou batalhar(2)'))
	# 	if resposta == 1:
	# 		continue
	# 	if resposta == 2:
	# 		batalha()
	# 	else:
	# 		print('nao existe essa opção')
	# 		continue