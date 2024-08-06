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

player = {  #Os atributos do player
    "nome": "Tecko",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dano": 25
}

def criar_npc(level): #Criamos uma função para criar npcs e recebendo o level para montar conforme o necessário
    #level = randint(0, 50) Criamos uma variável de level para que ele gere um e baseado nele você constroi os atributos do npc
    novo_npc = {           #Aqui criamos um dicionário com as informações/atributos e valores dos npcs
        "nome": f"Monstro {level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level
    }

    return novo_npc #Termina retornando o valor do novo_npc

def gerar_npcs(n_npcs):  #Criamos outra função para gerar o número de npcs que irão aparecer
    for x in range(n_npcs): #Gera uma lista de itens de acordo com o número de npcs que definimos
        npc = criar_npc(x + 1) #Geramos uma variável para pegar o valor que a função criar_npc está retornando e somamos +1 pra não comeãr com 0
        lista_npcs.append(npc) #Adicionamos os valores para a lista

def exibir_npcs(): #Ao invés de deixar solto criamo um função que exibe os npcs
    for npc in lista_npcs:
       exibir_npc(npc)

def exibir_npc(npc):
    print(f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}")

def exibir_player(): #A mesma função que o de mostrar as informações do npc mas agora com o player
    print(f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}")

def reset_player(): #Um reset de hp para o player a cada batalha
    player['hp'] = player['hp_max']

def reset_npc(npc): #Um reset para os NPCs a cada batalha, se não o player vai sempre ganhar direto por já estar 0
    npc['hp'] = npc['hp_max']

def level_up(): #Sistema para upar level
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 2
        player['hp_max'] += 20
        
def iniciar_bataha(npc):  #Função para mostrar a batalha junto com todas as outras.
    while player['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_infos_batalha(npc)
        print('-------------------\n')
    
    if player['hp'] > 0: #Condições para a vitória e derrota do player
        print(f"O {player['nome']} venceu!\nVocê ganhou {npc['exp']} de exp!")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f"O {npc['nome']} venceu! /n Tente de novo da próxima vez.")
        exibir_npcs()
    
    level_up()
    reset_player()
    reset_npc(npc)

def atacar_npc(npc): #Construimos uma função para o player atacar o npc
    npc['hp'] -= player['dano']

def atacar_player(npc): #função para o dano do npc no player
    player['hp'] -= npc['dano']

def exibir_infos_batalha(npc): #função para exibir informações da batalha
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}")


gerar_npcs(5) #Damos o valor da quantidade de numeros de npcs que queremos mostrar
#exibir_npcs() #Exibir as informações dos npcs

npc_selecionado = lista_npcs[0]
iniciar_bataha(npc_selecionado)
iniciar_bataha(npc_selecionado)
iniciar_bataha(npc_selecionado)
iniciar_bataha(npc_selecionado)
iniciar_bataha(npc_selecionado)
iniciar_bataha(npc_selecionado)