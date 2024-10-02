import random
from time import sleep

pnome = str(input('Olá, seja bem vindo a esse novo mundo de aventuras, aqui você poderá explorar, batalhar e upar o quanto quiser!\nPrimeiro me informe seu nome: '))

player = {
   "nome": pnome,
   "level": 1,
   "hp": 50,
   "hpmax": 50,
   "exp": 0,
   "expmax": 15,
   "dano": 15,
   "mana": 10,
   "manamax": 10,
   "dinheiro": 0
}

mochila = []

npc_lista = []

mapa_atual = []

andar_atual = 1

pos_jogador = (0, 0)

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
    npc_lista.clear()  # Limpar a lista de NPCs antes de gerar novos
    for x in range(n_npc):
        npc = criar_npc(x + 1)
        npc_lista.append(npc)

def exibir_npcs():
    for npc in npc_lista:
        exibir_npc(npc)

def exibir_npc(npc):
    print(f"Nome: {npc['nome']} // Level: {npc['level']} // HP: {npc['hp']} // EXP: {npc['exp']}")

def exibir_player():
    print(f"Nome: {player['nome']} // Level: {player['level']} // HP: {player['hp']}/{player['hpmax']} // EXP: {player['exp']}/{player['expmax']} // Dano: {player['dano']} // Dinheiro: {player['dinheiro']}")

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
        player['manamax'] += 5
        player['dano'] += 5

def exibir_infos_batalha(npc):
    if player['hp'] < 0:
        player['hp'] = 0

    if npc['hp'] < 0:
        npc['hp'] = 0

    print(f"{player['nome']}: {player['hp']}/{player['hpmax']}")
    print(f"{npc['nome']}: {npc['hp']}/{npc['hpmax']}")

def iniciar_batalha_coli(npc):
    c = 1
    while player['hp'] > 0 and npc['hp'] > 0:
        menu_batalha = int(input(f"Rodada {c} Monstro Apareceu!\nO que você gostaria de fazer?\n[1]Atacar\n[2]Ataque Especial\n[3]Usar Item\n[4]Parar\n"))
        if menu_batalha == 1:
            atacar_npc(npc)
            if npc['hp'] > 0:
                atacar_player(npc)
            exibir_infos_batalha(npc)
            print('-----------------------')

            if player['hp'] > 0:
                print(f"{player['nome']} venceu!\nVocê ganhou {npc['exp']} de experiência e {npc['level'] * 5} de dinheiro.")
                player['exp'] += npc['exp']
                player['dinheiro'] += npc['level'] * 5
            else:
                print(f"O {npc['nome']} venceu!\nTente de novo da próxima vez.")
                exibir_npcs()
            c += 1
        
        elif menu_batalha == 2:
            print('Escolha o ataque que vai usar')
            # Implementar ataques especiais aqui
            break
        
        elif menu_batalha == 3:
            usar_item()
        
        elif menu_batalha == 4:
            print("Você aguentou até aqui e saiu da arena!")
            break

    level_up()
    npc_reset(npc)
    sleep(2)
    mostrar_menu()

def mostrar_loja():
    lista_escolha = int(input("Olá seja bem vindo a loja da masmorra! O que gostaria de comprar?\n[1]Itens\n[2]Armaduras\n[3]Armas\n[4]Informações dos Produtos\n[5]Sair\n"))

    if lista_escolha == 1:
        sleep(1)
        mostrar_itens_loja()

    elif lista_escolha == 2:
        sleep(1)
        mostrar_armaduras_loja()
    
    elif lista_escolha == 3:
        sleep(1)
        mostrar_armas_loja()
    
    elif lista_escolha == 4:
        sleep(1)
        mostrar_info_produtos()

    elif lista_escolha == 5:
        print("Obrigado e volte sempre!")
        sleep(2)
        mostrar_menu()
    
    else:
        print("Escolha inválida!")
        sleep(1)
        mostrar_loja()

def mostrar_itens_loja():
    produto_escolha = int(input("Temos esses Itens Disponíveis:\n[1]Poção de Vida\n[2]Poção de Mana\n[3]Mini Elixir\n[4]Sair\n"))
    if produto_escolha == 1:
        if player['dinheiro'] >= 18:
            print('Aqui está!\nGostaria de mais alguma coisa?')
            mochila.append('Poção de Vida')
            player['dinheiro'] -= 18
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_itens_loja()
    elif produto_escolha == 2:
        if player['dinheiro'] >= 18:
            print('Aqui está!\nGostaria de mais alguma coisa?')
            mochila.append('Poção de Mana')
            player['dinheiro'] -= 18
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_itens_loja()
    elif produto_escolha == 3:
        if player['dinheiro'] >= 36:
            print('Aqui está!\nGostaria de mais alguma coisa?')
            mochila.append('Mini Elixir')
            player['dinheiro'] -= 36
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_itens_loja()
    elif produto_escolha == 4:
        sleep(1)
        mostrar_loja()
    else:
        print("Escolha inválida!")
        sleep(1)

def mostrar_armaduras_loja():
    armadura_escolha = int(input("Temos essas Armaduras Disponíveis:\n[1]Armadura de Fogo\n[2]Armadura de Vento\n[3]Armadura de Água\n[4]Sair\n"))
    if armadura_escolha == 1:
        if player['dinheiro'] >= 60:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mochila.append('Armadura de Fogo')
            player['dinheiro'] -= 60
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_armaduras_loja()
    elif armadura_escolha == 2:
        if player['dinheiro'] >= 60:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mochila.append('Armadura de Vento')
            player['dinheiro'] -= 60
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_armaduras_loja()
    elif armadura_escolha == 3:
        if player['dinheiro'] >= 60:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mochila.append('Armadura de Água')
            player['dinheiro'] -= 60
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_armaduras_loja()
    elif armadura_escolha == 4:
        sleep(1)
        mostrar_loja()
    else:
        print("Escolha Inválida!")
        sleep(1)

def mostrar_armas_loja():
    arma_escolha = int(input("Temos essas Armas Disponíveis:\n[1]Espada\n[2]Facas\n[3]Clava\n[4]Sair\n"))
    if arma_escolha == 1:
        if player['dinheiro'] >= 30:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mochila.append('Espada')
            player['dinheiro'] -= 30
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_armas_loja()
    elif arma_escolha == 2:
        if player['dinheiro'] >= 25:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mochila.append('Facas')
            player['dinheiro'] -= 25
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_armas_loja()
    elif arma_escolha == 3:
        if player['dinheiro'] >= 27:
            print("Aqui está!\nGostaria de mais alguma coisa?")
            mochila.append('Clava')
            player['dinheiro'] -= 27
        else:
            print("Você não tem dinheiro o suficiente!")
        sleep(1)
        mostrar_armas_loja()
    elif arma_escolha == 4:
        sleep(1)
        mostrar_loja()
    else:
        print("Escolha Inválida!")
        sleep(1)

def mostrar_info_produtos():
    print("Itens:\nPoção de Vida: +15 Vida - 18$\nPoção de Mana: +10 Mana - 18$\nMini Elixir: +15 Vida +10 Mana - 36$\nArmaduras:\nArmadura de Fogo: +15 Vida +Resistencia a Fogo - 60$\nArmadura de Água: +15 Mana +Resistencia a Água - 60$\nArmadura de Vento: +15 Velocidade +Resistencia a Vento - 60$\nArmas:\nEspada: +20 Dano - 30$\nFacas: +10 Dano +5 Velocidade - 25$\nClava: +15 Dano +3 Mana - 27$")
    sleep(2)
    mostrar_loja()

def restaurar_vida():
    if player['hp'] > player['hpmax']:
        player['hp'] = player['hpmax']
        print("Você recuperou a sua vida!")

def restaurar_status(restaurar_hp, restaurar_mana):
    player['hp'] += restaurar_hp
    if player['hp'] > player['hpmax']:
        player['hp'] = player['hpmax']
    
    player['mana'] += restaurar_mana
    if player['mana'] > player['manamax']:
        player['mana'] = player['manamax']

def usar_item():
    if not mochila:
        print("Sua Mochila está vazia!")
        sleep(1)
        mostrar_menu()
        return
    
    print("Itens na mochila:")
    for index, item in enumerate(mochila, 1):
        print(f"[{index}] {item}")

    while True:
        try:
            escolha_item = int(input("Escolha o número do item que quer usar: "))

            if escolha_item < 1 or escolha_item > len(mochila):
                print("Escolha inválida!")
                sleep(1)
                continue

            item_usado = mochila[escolha_item - 1]

            if item_usado == 'Poção de Vida':
                restaurar_status(15, 0)
                print("Você recuperou a sua vida!")
            
            elif item_usado == 'Poção de Mana':
                restaurar_status(0, 10)
                print("Você recuperou sua mana!")
            
            elif item_usado == "Mini Elixir":
                restaurar_status(15, 10)
                print("Você recuperou sua vida e sua mana!")
            
            mochila.remove(item_usado)
            break

        except ValueError as e:
            print("Entrada inválida. Tente novamente.")
            sleep(1)

    sleep(1)

def iniciar_batalha_exp(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
            menu_batalha = int(input("Um Monstro Apareceu!\nO que você gostaria de fazer?\n[1]Atacar\n[2]Ataque Especial\n[3]Usar Item\n[4]Fugir\n"))
            if menu_batalha == 1:
                atacar_npc(npc)
                if npc['hp'] > 0:
                    atacar_player(npc)
                exibir_infos_batalha(npc)
                print('-----------------------')

                if player['hp'] > 0:
                    print(f"{player['nome']} venceu!\nVocê ganhou {npc['exp']} de experiência e {npc['level'] * 5} de dinheiro.")
                    player['exp'] += npc['exp']
                    player['dinheiro'] += npc['level'] * 5
                else:
                    print(f"O {npc['nome']} venceu!\nTente de novo da próxima vez.")
                    exibir_npcs()
                break
        
            elif menu_batalha == 2:
                print('Escolha o ataque que vai usar')
                # Implementar ataques especiais aqui
                break
            
            elif menu_batalha == 3:
                usar_item()
            
            elif menu_batalha == 4:
                print("Você fugiu!")
                break

            else:
                print('Escolha inválida!')

    level_up()
    npc_reset(npc)
    sleep(2)

def gerar_mapas(largura, altura):
    mapa = []
    for _ in range(altura):
        linha = []
        for _ in range(largura):
            tipo_casa = random.choices(['vazia', 'monstro', 'baú', 'escada', 'saída'], [5, 3, 1, 1, 1])[0]
            linha.append(tipo_casa)
        mapa.append(linha)
    
    return mapa

def exibir_mapa(mapa, pos_jogador):
    for y in range(len(mapa)):
        linha = ""
        for x in range(len(mapa[0])):
            if (x, y) == pos_jogador:
                linha += "P "  # Representa o jogador
            elif mapa[y][x] == 'vazia':
                linha += "X "
            elif mapa[y][x] == 'monstro':
                linha += "M "
            elif mapa[y][x] == 'baú':
                linha += "B "
            elif mapa[y][x] == 'escada':
                linha += "E "
            elif mapa[y][x] == 'saída':
                linha += "S"
        print(linha)
    print()

def movimentar_jogador(pos_jogador, direcao, largura, altura):
    x, y = pos_jogador
    if direcao == 'w' and y > 0:
        y -= 1
    elif direcao == 's' and y < altura - 1:
        y += 1
    elif direcao == 'a' and x > 0:
        x -= 1
    elif direcao == 'd' and x < largura - 1:
        x += 1
    return (x, y)

def interagir_casa(mapa, pos_jogador):
    global andar_atual  # Declare 'andar_atual' como global
    x, y = pos_jogador
    casa = mapa[y][x]
    if casa == 'monstro':
        print("Você encontrou um monstro!")
        gerar_npcs(andar_atual)
        npc_selecionado = npc_lista[0]
        iniciar_batalha_exp(npc_selecionado)
    elif casa == 'baú':
        print("Você encontrou um baú!")
        mochila.append(random.choices(['Poção de Vida', 'Poção de Mana' ]))
    elif casa == 'escada':
        print("Você encontrou uma escada para o próximo andar!")
        andar_atual += 1
        player['level'] = andar_atual  # Atualiza o nível do jogador com o andar atual
        player['exp'] = 0
        player['expmax'] = 15 * andar_atual
        gerar_npcs(andar_atual)
        mapa_atual[:] = gerar_mapas(5, 5)  # Gera um novo mapa 5x5
        pos_jogador = (0, 0)  # Reseta a posição do jogador
        explorar_mapa(mapa_atual)
    elif casa == 'vazia':
        print("Você está em uma casa vazia.")
    
    elif casa == 'saída':
        escolha_sair = input("Você encontrou uma saída, gostaria de voltar? [S/N]\n")
        if escolha_sair.lower() == 's':
            mostrar_menu()
        elif escolha_sair.lower() == 'n':
            print('Que a aventura continue!') 
        else:
            print('Escolha inválida')



def explorar_mapa(mapa):
    largura = len(mapa[0])
    altura = len(mapa)
    pos_jogador = (0, 0)  # Começa no canto superior esquerdo
    while True:
        exibir_mapa(mapa, pos_jogador)
        comando = input("Para onde você deseja ir? (w/a/s/d para mover, q para sair): ")
        if comando == 'q':
            break
        elif comando in ['w', 'a', 's', 'd']:
            nova_pos = movimentar_jogador(pos_jogador, comando, largura, altura)
            if nova_pos != pos_jogador:
                pos_jogador = nova_pos
                interagir_casa(mapa, pos_jogador)
        else:
            print("Comando inválido.")

def mostrar_menu():
    menu = int(input(f"{pnome} o que gostaria de fazer agora?\n[1]Explorar\n[2]Coliseu\n[3]Comprar Itens\n[4]Status\n[5]Mochila\n[6]Sair\n"))
    if menu == 1:
        sleep(1)
        mapa = gerar_mapas(5, 5)  # Cria um mapa 5x5
        explorar_mapa(mapa)  # Permite ao jogador explorar o mapa
    
    elif menu == 2:
        sleep(1)
        print("Bem vindo ao Coliseu, aqui você trava batalhas até não aguentar mais.\n Daremos ínicio as batalhas!\n")
        gerar_npcs(1)
        npc_selecionado = npc_lista[0]
        iniciar_batalha_coli(npc_selecionado)
    
    elif menu == 3:
        sleep(1)
        mostrar_loja()
    
    elif menu == 4:
        sleep(1)
        exibir_player()
        mostrar_menu()
    
    elif menu == 5:
        sleep(1)
        print(mochila)
        mostrar_menu()

    elif menu == 6:
        sleep(1)
        print("Até uma outra aventura!")
        return False
    else:
        print("Escolha inválida!")

    sleep(2)

while True:
    if not mostrar_menu():
        break










