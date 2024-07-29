"""lista_npcs = [
    {"nome": "Minimonstrinho", "level": 1},
    {"nome": "Monstrinho", "level": 2},
    {"nome": "Monstro", "level": 3},
    {"nome": "Monstrão", "level": 4},
    {"nome": "Boss", "level": 5},
]
#Aqui criamos uma lista para os npcs inlundo dicionários dentro dela de cada um

for npc in lista_npcs:
    print(f"Nome: {npc['nome']}  // Level: {npc['level']}")"""

from random import randint

lista_npcs = [] #Criamos uma lista vazia

player = {
    "nome": "Tecko",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "dano": 25
}

def criar_npc(): #Criamos uma função para criar npcs
    level = randint(0, 50) #Criamos uma variável de level para que ele gere um e baseado nele você constroi os atributos do npc
    novo_npc = {           #Aqui criamos um dicionário com as informações/atributos e valores dos npcs
        "nome": f"Monstro {level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level
    }

    return novo_npc #Termina retornando o valor do novo_npc

def gerar_npcs(n_npcs):  #Criamos outra função para gerar o número de npcs que irão aparecer
    for x in range(n_npcs): #Gera uma lista de itens de acordo com o número de npcs que definimos
        novo_npc = criar_npc() #Geramos uma variável para pegar o valor que a função criar_npc está retornando
        lista_npcs.append(novo_npc) #Adicionamos os valores para a lista

def exibir_npcs(): #Ao invés de deixar solto criamo um função que exibe os npcs
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']}")


gerar_npcs(5) #Damos o valor da quantidade de numeros de npcs que queremos mostrar
exibir_npcs()