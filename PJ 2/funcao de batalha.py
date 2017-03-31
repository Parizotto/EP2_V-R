import random
import json

def escolher (database):
	inimigo = database[random.randrange(len(database))]
	return inimigo

with open("database.json") as arquivo:
    dados = json.load(arquivo)

database = dados["database"]
player = dados["player"]
inimigo = escolher(database)

print("Nome = {0}".format(inimigo["nome"]))
print("Poder = {0}".format(inimigo['poder']))
print("Vida = {0}".format(inimigo["vida"]))
print("Defesa = {0}".format(inimigo["defesa"]))
