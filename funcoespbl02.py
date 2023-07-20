import keyboard
import os
import time

def menu(): #Função para abrir o menu do jogo
	matriz_Menu = [[' ','Jogar',' '],[' ','Recordes',' '],[' ','Sobre',' '],[' ','Sair',' ']] #Criação da matriz do menu
	linha_Menu = 0 
	while not keyboard.is_pressed('enter'): #Loop do menu do jogo que só é finalizado quando o usuário pressiona a tecla ENTER
		os.system('cls')
		print('''
     ___           _______ ___________  _______  ______     ______    __   _______       _______
    /   \         /       |           ||   ____||   _  \   /  __  \  |  | |       \     /       |
   /  ^  \       |   (----`---|  |----`|  |__   |  |_)  | |  |  |  | |  | |  .--.  |   |   (----`
  /  /_\  \       \   \       |  |     |   __|  |      /  |  |  |  | |  | |  |  |  |    \   \    
 /  _____  \  .----)   |      |  |     |  |____ |  |\  \  |  `--'  | |  | |  '--'  |.----)   |   
/__/     \__\ |_______/       |__|     |_______|| _| `._|  \______/  |__| |_______/ |_______/                                                                     
''')
		print('============ MENU', 80*'=', '\n')
		for linha in range(4): #Repetição que imprime na tela a matriz do menu
			for coluna in range(3):
				print(matriz_Menu[linha][coluna], end = ' ')
			print()
		if keyboard.is_pressed('up') and linha_Menu > 0: #Condicional para o usuário selecionar a opção acima
			linha_Menu -= 1
			time.sleep(0.5)
		if keyboard.is_pressed('down') and linha_Menu < 3: #Condicional para o usuário selecionar a opção abaixo
			linha_Menu += 1
			time.sleep(0.5)
		matriz_Menu = [[' ','Jogar',' '],[' ','Recordes',' '],[' ','Sobre',' '],[' ','Sair',' ']] 
		matriz_Menu[linha_Menu][0] = '< '
		matriz_Menu[linha_Menu][2] = ' >'
		
	return linha_Menu + 1

def leiaInt(x): #Função para identificar se o valor lido foi um número inteiro
	ok = False
	valor = 0
	abilitadorLoop = 0 #Variável para abilitar o loop while
	while abilitadorLoop == 0:
		n = str(input(x))
		if n.isnumeric():
			valor = int(n)
			ok = True
		else: 
			print('\nErro! Digite um número válido.')
		if ok:
			abilitadorLoop = 1

	return valor

def matriz_Inicial(matriz): #Função que cria uma matriz 35 por 36
	for linha in range(35): 
		linhas = []
		for coluna in range(36):
			linhas.append(' ')
		matriz.append(linhas)

	return matriz

def objetos(linha, frame, aleatorio, novamatriz): #Função que coloca os objetos Nave e Meteoro dentro da matriz Novamatriz
	for indice in range(35): #Condicional que adiciona a barreira que limita o jogo na horizontal
		novamatriz[indice][35] = '|'

	#Criação da nave caractere a caractere
	novamatriz[34][frame] = '◢'
	novamatriz[34][frame+1] = '▮'
	novamatriz[34][frame+2] = '▮'
	novamatriz[34][frame+3] = '▮'
	novamatriz[34][frame+4] = '◣'
	novamatriz[33][frame+1] = '◢'
	novamatriz[33][frame+2] = '▮'
	novamatriz[33][frame+3] = '◣'
	novamatriz[32][frame+2] = '△'

	#Criação do meteoro caractere a caractere
	novamatriz[linha][aleatorio+2] = '*'
	novamatriz[linha][aleatorio+3] = '*'
	novamatriz[linha][aleatorio+4] = '*'
	if linha < 34:
		novamatriz[linha+1][aleatorio+1] = '*'
		novamatriz[linha+1][aleatorio+2] = '*'
		novamatriz[linha+1][aleatorio+3] = '*'
		novamatriz[linha+1][aleatorio+4] = '*'
		novamatriz[linha+1][aleatorio+5] = '*'
	if linha < 33:
		novamatriz[linha+2][aleatorio] = '*'
		novamatriz[linha+2][aleatorio+1] = '*'
		novamatriz[linha+2][aleatorio+2] = '*'
		novamatriz[linha+2][aleatorio+3] = '*'
		novamatriz[linha+2][aleatorio+4] = '*'
		novamatriz[linha+2][aleatorio+5] = '*'
		novamatriz[linha+2][aleatorio+6] = '*'
	if linha < 32:
		novamatriz[linha+3][aleatorio+1] = '*'
		novamatriz[linha+3][aleatorio+2] = '*'
		novamatriz[linha+3][aleatorio+3] = '*'
		novamatriz[linha+3][aleatorio+4] = '*'
		novamatriz[linha+3][aleatorio+5] = '*'
	if linha < 31:
		novamatriz[linha+4][aleatorio+2] = '*'
		novamatriz[linha+4][aleatorio+3] = '*'
		novamatriz[linha+4][aleatorio+4] = '*'
	
	return novamatriz

def misselup(existe, novamatriz, missel, frame_Movel): #Função que altera a posição do míssel a cada loop
	if existe and novamatriz[missel - 2][frame_Movel] == ' ': 
		novamatriz[missel][frame_Movel] = 'o'
		if missel > 0:
			missel -= 1
		else:
			existe = False
			missel = 31

	return novamatriz, missel, existe

def print_Vazio(novamatriz): #Função que Imprime na tela a matriz após as mudanças dos objetos
	for linha in range(35):
		for coluna in range(36):
			print(novamatriz[linha][coluna], end = ' ')
		print()

def colisao_Nave(novamatriz, frame): #Função que retorna a variável exit caso a nave colida com o meteoro
	if novamatriz[32][frame+2] == '*':
		exit = True
		return exit
	if novamatriz[33][frame+1] == '*':
		exit = True
		return exit
	if novamatriz[33][frame+3] == '*':
		exit = True
		return exit
	if novamatriz[34][frame] == '*':
		exit = True
		return exit
	if novamatriz[34][frame+4] == '*':
		exit = True
		return exit

def colisao_Missel(frame_Movel, missel, novamatriz, meteoros, pontos, existe, quebra): #Função que checa se o meteoro colidiu com o míssel

	if novamatriz[missel][frame_Movel] == '*' and existe:
		novamatriz[missel][frame_Movel] = ' '
		meteoros = meteoros + 1
		pontos = pontos + 7
		existe = False
		missel = 31
		quebra = True

		return novamatriz, novamatriz[missel][frame_Movel], meteoros, pontos, existe, missel, quebra
	else: 

		return novamatriz, novamatriz[missel][frame_Movel], meteoros, pontos, existe, missel, quebra

def matriz_Vazia(): #Função que recria a matriz Novamatriz com todas suas coordenadas vazias 
	novamatriz = []
	for linha in range(35):
		linhas = []
		for coluna in range(36):
			linhas.append(' ')
		novamatriz.append(linhas)

	return novamatriz

def comandos_Nave(frame): #Função que move a nave para a direita e esquerda caso o usuário pressione as teclas RIGHT or LEFT
	if keyboard.is_pressed('left') and frame > 0:
		frame = frame - 1
	if keyboard.is_pressed('right') and frame + 4 < 34:
		frame = frame + 1
	
	return frame

def pause(): #Função de pause e despause do jogo
	if keyboard.is_pressed('p') == True: #Condicional que pausa o jogo caso o usuário pressione a tecla P
		print('JOGO PAUSADO\nPressione "P" novamente para despausar.')
		time.sleep(1)
		while keyboard.is_pressed('p') == False: #Condicional que despausa o jogo caso o usuário pressione a tecla P
			time.sleep(0.05)

def gameover(pontos, lista_Nomes, lista_Recordes): #Função com as mensagens caso o jogador tenha perdido e realoca sua pontuação e nome na respectiva lista
	chave = 0
	while chave != '000': #Condicional que é finalizada caso o usuário aperte a tecla ENTER
		print('''
  _______      ___       ___  ___   _______      ______   ____    ____  _______  ______      
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \_
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `.__|
                                                                                          
''')
		print('Aperte "Enter" para continuar.')
		chave = input() #Variável criada para evitar erros
		if keyboard.is_pressed('enter'):
			chave = '000'
		os.system('cls')

	nome = input('\nQual seu nome de usuário? ')
	while nome == '':	
		nome = input('\nNome inválido! Qual seu nome de usuário? ') 
	time.sleep(0.5)
	
	#Bloco de código que realoca as 5 maiores pontuações com o nome de cada jogador
	if not lista_Recordes or pontos > lista_Recordes[0] or lista_Nomes[0] == '???':
		lista_Recordes.insert(0, pontos)
		lista_Nomes.insert(0, nome)
	elif len(lista_Recordes) == 1 or pontos > lista_Recordes[1] or lista_Nomes[1] == '???':
		lista_Recordes.insert(1, pontos)
		lista_Nomes.insert(1, nome)
	elif len(lista_Recordes) == 2 or pontos > lista_Recordes[2] or lista_Nomes[2] == '???':
		lista_Recordes.insert(2, pontos)
		lista_Nomes.insert(2, nome)
	elif len(lista_Recordes) == 3 or pontos > lista_Recordes[3] or lista_Nomes[3] == '???':
		lista_Recordes.insert(3, pontos)
		lista_Nomes.insert(3, nome)
	elif len(lista_Recordes) == 4 or pontos > lista_Recordes[4] or lista_Nomes[4] == '???':
		lista_Recordes.insert(4, pontos)
		lista_Nomes.insert(4, nome)
	else:
		if len(lista_Recordes) > 5:
			lista_Recordes.pop()
			lista_Nomes.pop()

	return (lista_Nomes, lista_Recordes)

def top5(lista_Nomes, lista_Recordes): #Função que imprime na tela os 5 melhores jogadores de acordo com suas pontuações
	os.system('cls')
	print('\nTOP 5 RANQUEADOS\n')
	for indice in range(len(lista_Nomes)):
		if indice < 5:
			print('%s°| %s: %s' % (indice+1, lista_Nomes[indice], lista_Recordes[indice]))
	print('\nPressione ESC para voltar ao menu principal.')

	return

def sobre(): #Função que printa as informações do jogo ASTEROIDS
	os.system('cls')
	print('\nVoce escolheu ver sobre o jogo!\n')
	print('Esta é uma versão de Asteroids, um jogo casual de ação, desenvolvida em 2021 pelo estudante de engenharia de computação Hélio J. da S. Júnior.\nVocê deve destruir a maior quantidade de asteroides possíveis com a sua nave que atira potentes mísseis para conquistar pontos e entrar no rank dos 5 melhores jogadores.')
	print('\nControles do jogo:\nSPACE -> A nave realiza um disparo\nLEFT -> Movimenta a nave para a esquerda\nRIGHT -> Movimenta a nave para a direita\nP -> Pausa o jogo\nESC -> Finaliza o jogo\n\nAlém do ESC, a jogatina também será finalizada caso 10 asteroides não sejam destruidos ou se um deles atingir a nave.')
	print('\nPressione ESC para voltar ao menu principal.')

	return	
