dict_romain_vers_arabe ={
'I':1,
'II':2,
'III':3,
'IV':4,
'V':5,
'VI':6,
'VII':7,
'VIII':8,
'IX':9,
'X':10
}

list_a_tester = [
'I',
'II',
'III',
'V',
'X'
]

def
romain_vers_arabe(chiffre_romain):
print('Ton chiffre romain en arabe donne :')
print( dict_romain_vers_arabe[chiffre_romain] )


for chiffre
in list_a_tester :
romain_vers_arabe(chiffre)
# Fonction pour traduire le romain vers l'arabe
def
function_pour_traduire_le_romain_vers_arabe(chiffre_romain):
if chiffre_romain
==
'I':
print(1)
elif chiffre_romain
==
'II':
print(2)
elif chiffre_romain
==
'III':
print(3)
elif chiffre_romain
==
'IV':
print(4)

'''
membre_du_lab = [
{'sakada':'lunette', 'andy':'pas lunette', 'Laurent':'lunette', 'Christophe':'pas lunette'},
{'sakada':'entends mal', 'andy':'entends bien', 'Laurent':'entends mal pour un musicience', 'Christophe':'entends bien'}
]
'''


membre_du_lab = [
{
'prenom':'Sakada',
'vue':'lunette',
'ouie':'entends mal'
},

{
'prenom':'Andy',
'vue':'pas lunette',
'ouie':'entends bien'
},

{
'prenom':'Laurent',
'vue':'lunette',
'ouie':'entends mal pour un musicien'
},

{
'prenom':'Christophe',
'vue':'pas lunette',
'ouie':'entends bien'
},
]

for membre
in membre_du_lab:
if membre['vue']
==
'lunette':
print(membre['prenom'])
