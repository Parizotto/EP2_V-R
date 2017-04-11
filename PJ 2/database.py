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
{
	"nome" : "kevin",
	"poder" : 26,
	"vida" : 350,
	"defesa": 9 
},

{
	"nome" : "Abc",
	"poder" : 30,
	"vida" : 50,
	"defesa" : 18
},
{
	"nome" : "Venossauro",
	"poder" : 60,
	"vida" : 500,
	"defesa" : 40
},
{
	"nome" : "Ivossauro",
	"poder" : 40,
	"vida" : 380,
	"defesa" : 25
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