import pickle
database=[{
	"nome" : "Squirtle",
	"poder" : 20,
	"vida" : 200,
	"defesa" : 12
},
{
	"nome" : "caterpie",
	"poder" : 25,
	"vida" : 100,
	"defesa" : 10
},
{
	"nome" : "Bulbasaur",
	"poder" : 15,
	"vida" : 300,
	"defesa" : 11
},
{
	"nome" : "Pidgey",
	"poder" : 27,
	"vida" : 200,
	"defesa": 13 
},
{"player": {
"nome" : "pikachu",
"poder" : 10,
"vida" : 150,
"defesa" : 12 }
}
]
with open ('database.pickle','wb') as arquivo:
	pickle.dump(database,arquivo)