'''
Autor: Hélio José da Silva Júnior
Componente Curricular: MI - Algoritmos I
Concluido em: 25/04/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação. 
'''

from funcoespbl02 import *
import keyboard
import os
import time
import random

lista_Nomes = ['???','???','???','???','???'] 
lista_Recordes = [0, 0, 0, 0, 0]
index = 0 
matriz = []
escolha = 0 #Habilitador do loop

while escolha != 4:
    escolha = menu() #Chama a função menu

    if escolha == 1: #Condicional caso o usuário tenha selecionado a opção 'Jogar'
        print('\nVoce escolheu jogar!\n')

        matriz_Inicial(matriz)

        #Atribuição das variáveis necessárias para o funcionamento do jogo
        novamatriz = matriz
        frame = 18 #18 para a nave surgir no meio da tela
        frame_Movel = 20
        missel = 31 #linha que o míssel será disparado
        existe = False #existe míssel na tela?
        colisao = False
        exit = False #exit == saída em inglês
        meteoros = -1
        pontos = 0
        vida = 10
        asteroids = 0

        while vida > 0 and exit == False: #Loop com o jogo rodando, o mesmo é finaliza quando a vida acaba ou o meteoro colide com a nave
            aleatorio = random.randint(1,27) #Gera um número aleatório que será a posição referencial do próximo meteoro
            meteoros += 1 
            linha = 0

            while linha < 35: #Loop que gera a linha referencial do meteoro
                objetos(linha, frame, aleatorio, novamatriz)

                if keyboard.is_pressed('space'): #Condicional para o disparo do meteoro caso o espaço do teclado for pressionado                   
                    if missel == 31 and existe == False:
                        frame_Movel = frame+2 #Frame móvel é a coluna na qual míssel foi disparado
                        existe = True

                (novamatriz, missel, existe) = misselup(existe, novamatriz, missel, frame_Movel)

                if novamatriz[34][aleatorio] == '*': #Condicional que percebe quando a nave está na última linha, consequentemente tirando uma vida do usuário
                    vida = vida - 1
                    asteroids += 1

                print_Vazio(novamatriz)

                if colisao_Nave(novamatriz, frame) == True: #Condicional que finaliza o jogo caso o meteoro colida com a nave
                    exit = True
                    linha = 34

                quebra = False
                novamatriz, novamatriz[missel][frame_Movel], meteoros, pontos, existe, missel, quebra = colisao_Missel(frame_Movel, missel, novamatriz, meteoros, pontos, existe, quebra)

                if quebra: #Condicional que quebra o loop caso o meteoro colida com o missel
                    break
                
                novamatriz = matriz_Vazia()

                frame = comandos_Nave(frame)
                
                if keyboard.is_pressed('esc') == True: #Condicional que finaliza a jogatina caso o usuário pressione a tecla ESC
                    exit = True
                    linha = 34
                
                pause()
                
                print('Pontos: %d \nVidas restantes: %d \nAsteroides não destruidos: %d' % (pontos, vida, asteroids)) #Imprime na tela os pontos, os asteroides não destruidos e a vida restante do usuário

                time.sleep(0.05) #Determina o tempo de execução do loop como 0.01 segundos
                os.system('cls') #Atualiza a tela

                linha += 1 

        lista_Nomes, lista_Recordes = gameover(pontos, lista_Nomes, lista_Recordes)       

    elif escolha == 2: #Condicional caso o usuario tenha selecionado a opcao 'Recordes'
        while not keyboard.is_pressed('esc'):
            top5(lista_Nomes, lista_Recordes)


    elif escolha == 3: #Condicional caso o usuario tenha selecionado a opcao 'Sobre'
        while not keyboard.is_pressed('esc'):
            sobre()

    elif escolha == 4: #Condicional caso o usuario tenha selecionado a opcao 'Sair'
        print('\nVocê escolheu sair do jogo.')

