PERDEU = 0
VENCEU = 1
import random
import time, sys
import json
def batalha(player, inimigo):
	with open("database.json") as arquivo:
		dados = json.load(arquivo)
	#Aleatoriedade nas fugas das batalhas
	fugir_lento = [1,2,3,4,5,6,7,8,9,10]
	fugir_rapido = [1,2,3,4,5]

	run= ("Fugiu")
	database = dados["database"]
	player = dados["player"]
	while True:
		#Frases do jogo com e sem delay 
		resposta = input("\nvocê deseja:\n1 - fugir\n    ou\n2 - batalhar\n")
		conseguiu = ("\nsucesso na fuga\n")
		nao_conseguiu =("\nNão conseguiu fugir\nBatalhando em:\n3\n2\n1\n")
		batalhando= ("batalhando em:")
		numeros =("\n3\n2\n1\n")
		#Inicio das opções de batalha e fuga 
		if resposta == "1":
			if (player["poder"]) >= (inimigo["poder"]):
				run_fast = fugir_rapido[random.randrange(len(fugir_rapido))]
				if run_fast == 1 or run_fast == 3 or run_fast == 5:
					#delay da frase
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
					#Se não conseguir fugir, a batalha será iniciada
					while player["vida"]>0 and inimigo["vida"]>0:
						#Inicio da aleatoridade das batalhas,utilizando intervalos de tempo relacionados a ganho ou perda de poder
						if inimigo["tipo"] == "normal":
							n=random.randint(1,12)
							if n<=3:
								player["poder"]+=5
							elif n>=10:
								inimigo["poder"]+=5
							else:
								x=random.uniform(0.75,1.15)
								y=random.uniform(0.75,1.3)
								player["defesa"]*=(x//1)
								inimigo["defesa"]*=(y//1)

						if inimigo["tipo"] == "fogo" or "planta":
							m=random.randint(1,20)
							if m<=4:
								player["poder"]+=8
							elif  m==5:
								player["poder"]+=18
							elif m>5 and m<=9:
								inimigo["poder"]+=8
							elif m==11:
								inimigo["poder"]+=18
						# Este else remete aos pokemons do tipo agua
						else:
							o=random.randint(1,15)
							if o<=5:
								player["poder"]+=8
								player["defesa"]+=2
							elif o>5:
								player["poder"]-=5
								player["defesa"]-=2

						inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
						player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
<<<<<<< HEAD
=======
						print("a vida do seu pokemon: {0}".format(player["vida"]))

>>>>>>> ed2702e6f93bdaefaece29a3d55c8ba5db1f381c
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
						#Aleatorio tipo normal
						if inimigo["tipo"] == "normal":
							n=random.randint(1,12)
							if n<=3:
								player["poder"]+=5
							elif n>=10:
								inimigo["poder"]+=5
							else:
								x=random.uniform(0.75,1.15)
								y=random.uniform(0.75,1.3)
								player["defesa"]*=(x//1)
								inimigo["defesa"]*=(y//1)
						#Aleatorio tipo fogo e planta
						if inimigo["tipo"] == "fogo" or "planta":
							m=random.randint(1,20)
							if m<=4:
								player["poder"]+=8
							elif  m==5:
								player["poder"]+=18
							elif m>5 and m<=9:
								inimigo["poder"]+=8
							elif m==11:
								inimigo["poder"]+=18
						# Este else remete aos pokemons do tipo agua
						else:
							o=random.randint(1,15)
							if o<=5:
								player["poder"]+=8
								player["defesa"]+=2
							elif o>5:
								player["poder"]-=5
								player["defesa"]-=2		

						inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
						player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
<<<<<<< HEAD
=======
						print("a vida do seu pokemon: {0}".format(player["vida"]))

>>>>>>> ed2702e6f93bdaefaece29a3d55c8ba5db1f381c
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
				#Aleatoriedade para tipo normal
				if inimigo["tipo"] == "normal":
						n=random.randint(1,12)
						if n<=3:
							player["poder"]+=5
						elif n>=10:
							inimigo["poder"]+=5
						else:
							x=random.uniform(0.75,1.15)
							y=random.uniform(0.75,1.3)
							player["defesa"]*=(x//1)
							inimigo["defesa"]*=(y//1)
				#Aleatoriedade para pokemons tipo fogo e planta
				if inimigo["tipo"] == "fogo" or "planta":
					m=random.randint(1,20)
					if m<=4:
						player["poder"]+=8
					elif  m==5:
						player["poder"]+=18
					elif m>5 and m<=9:
						inimigo["poder"]+=8
					elif m==11:
						inimigo["poder"]+=18
				# Este else remete aos pokemons do tipo agua
				else:
					o=random.randint(1,15)
					if o<=5:
						player["poder"]+=8
						player["defesa"]+=2
					elif o>5:
						player["poder"]-=5
						player["defesa"]-=2
				# Equaçoes para ocorrer as batalhas e obter um resultado
				inimigo["vida"] = inimigo["vida"] + ( inimigo["defesa"] -player["poder"])
				player["vida"] = player["vida"] + (player["defesa"]-inimigo["poder"] )
<<<<<<< HEAD
=======
				print("a vida do seu pokemon: {0}".format(player["vida"]))
				print ("poder: {0}".format(player["poder"]))

>>>>>>> ed2702e6f93bdaefaece29a3d55c8ba5db1f381c
			if inimigo["vida"]<=0 :
				return VENCEU
				break
			if player["vida"] <=0:
				return PERDEU
				break
		else:
			print("nao existe")