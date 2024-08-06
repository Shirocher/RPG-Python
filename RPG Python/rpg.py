from time import sleep

pnome = str(input('Olá, seja bem vindo a esse novo mundo de aventuras, aqui você poderá explorar, batalhar e upar o quanto quiser!\nPrimeiro me informe seu nome: '))

player = {
   "nome": pnome,
   "level": 1,
   "hp": 50,
   "hpmax": 50,
   "exp": 0,
   "expmax": 15,
   "dano": 15
}

mochila = []

npc_lista = []

def criar_npc(level):
    novo_npc = {
        "nome": f"Monstro {level}",
        "level": level,
        "hp": 100 * level,
        "hpmax": 100 * level,
        "exp": 7 * level,
        "dano": 5 * level
    }

    return novo_npc

def gerar_npcs(n_npc):
    for x in range (n_npc):
        npc = criar_npc (x + 1)
        npc_lista.append(npc)

def exibir_npcs():
    for npc in npc_lista:
        exibir_npc(npc)

def exibir_npc(npc):
    print(f"Nome: {npc['nome']} // Level: {npc['level']} // HP: {npc['hp']} // EXP: {npc['exp']}")

def exibir_player():
    print(f"Nome: {player['nome']} // Level: {player['level']} // HP: {player['hp']}/{player['hpmax']} // EXP: {player['exp']}/{player['expmax']} // Dano: {player['dano']}")

def atacar_npc(npc):
    npc['hp'] -= player['dano']

def atacar_player(npc):
    player['hp'] -= npc['dano']

def player_reset():
    player['hp'] = player['hpmax']

def npc_reset(npc):
    npc['hp'] = npc['hpmax']

def level_up():
    if player['exp'] >= player['expmax']:
        print("Parabéns, você subiu de nível!")
        player['level'] += 1
        player['exp'] = 0
        player['expmax'] = player['expmax'] * 2
        player['hpmax'] += 20

def exibir_infos_batalha(npc):
    if player['hp'] < 0:
        player['hp'] = 0

    elif npc['hp'] < 0:
        npc['hp'] = 0

    print(f"{player['nome']}: {player['hp']}/{player['hpmax']}")
    print(f"{npc['nome']}: {npc['hp']}/{npc['hpmax']}")

def iniciar_batalha(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_infos_batalha(npc)
        print('-----------------------')

    if player['hp'] > 0:
        print(f"{player['nome']} venceu!\nVocê ganhou {npc['exp']} de experiência.")
        player['exp'] += npc['exp']
    else:
        print(f"O {npc['nome']} venceu! /n Tente de novo da próxima vez.")
        exibir_npcs()

    level_up()
    player_reset()
    npc_reset(npc)

def mostrar_loja():
    lista_escolha = int(input("Olá seja bem vindo a loja da masmorra! O que gostaria de comprar?\n[1]Itens\n[2]Armaduras\n[3]Armas\n[4]Informações dos Produtos\n[5]Sair\n"))

    if lista_escolha == 1:
        mostrar_itens_loja()

def mostrar_itens_loja():
        produto_escolha = int(input("Temos esses Itens Disponíveis:\n[1]Poção de Vida\n[2]Poção de Mana\n[3]Mini Elixir\n[4]Sair\n"))
        if produto_escolha == 1:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mostrar_itens_loja()
        elif produto_escolha == 2:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mostrar_itens_loja()
        elif produto_escolha == 3:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mostrar_itens_loja()
        elif produto_escolha == 4:
            mostrar_loja()
        else:
            print("Escolha inválida!")

def mostrar_menu():
    menu = int(input(f"{pnome} o que gostaria de fazer agora?\n[1]Explorar\n[2]Batalhar\n[3]Comprar Itens\n[4]Status\n[5]Mochila\n[6]Sair\n"))
    if menu == 2:
        gerar_npcs(1)
        npc_selecionado = npc_lista[0]
        iniciar_batalha(npc_selecionado)
    
    elif menu == 3:
        mostrar_loja()
    
    elif menu == 4:
        exibir_player()

    elif menu == 6:
        print("Até uma outra aventura!")

    else:
        print("Escolha inválida!")

    sleep(2)

    

while True:
    mostrar_menu()
    '''if menu == 2:
        gerar_npcs(1)
        npc_selecionado = npc_lista[0]
        iniciar_batalha(npc_selecionado)
    
    elif menu == 3:
        l_escolha = int(input("Olá seja bem vindo a loja da masmorra! O que gostaria de comprar?\n[1]Itens\n[2]Armaduras\n[3]Armas\n[4]Informações dos Produtos\n[5]Sair"))
        if l_escolha == 1:
            print("Temos esses Itens Disponíveis:\n[1]Poção de Vida\n[2]Poção de Mana\n[3]Mini Elixir")
        elif l_escolha == 2:
            print("Temos essas Armaduras Disponíveis:\n[1]Armadura de Fogo\n[2]Armadura de Vento\n[3]Armadura de Água")
    elif menu == 4:
        exibir_player()
    elif menu == 6:
        break
    else:
        print("Escolha inválida!")

    sleep(2)'''
'''gerar_npcs(5)

npc_selecionado = npc_lista[0]
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)'''
