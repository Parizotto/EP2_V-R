PERDEU = 0
VENCEU = 1

def batalha(player, inimigo):
	while player[vida]>0 and inimigo[vida]>0:
		Vidainimigo = inimigo[vida] - ( player[poder] - inimigo[defesa])
		if Vidainimigo <=0 :
			return VENCEU # conferir se deve ser retotnado 1 ou venceu
		Vidaplayer = player[vida] - (inimido[poder] - player[defesa])
		if Vidaplayer <=0:
			return PERDEU	
	# if (inimigo['poder']) >= (player['poder']):
	# 	batalha()
	# else:
	# 	resposta= int(input('você quer fugir(1) ou batalhar(2)'))
	# 	if resposta == 1:
	# 		continue
	# 	if resposta == 2:
	# 		batalha()
	# 	else:
	# 		print('nao existe essa opção')
	# 		continue