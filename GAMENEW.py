# -- coding: utf-8 --
import pygame, sys
from pygame.locals import *
from random import randint
import time

__BY__= 'Feito por : Roni And Bruno'
__VER__= 'Version: 1.2'
#Audio
pygame.mixer.init()
pygame.mixer.music.load('audios/Tetris.ogg')
pygame.mixer.music.play()
derrota = pygame.mixer.Sound('audios/morte.wav')
comeu = pygame.mixer.Sound('audios/comeu.wav')
clique = pygame.mixer.Sound('audios/clique.wav')
pygame.mixer.music.set_volume(0.5)


def verificaMouse(img_botao,pos_botao,pos_mouse):
    img_x, img_y = pos_botao
    img_w, img_h = img_botao.get_size()
    varia_x = img_x + img_w
    varia_y = img_y + img_h
    if pos_mouse[0] > img_x and pos_mouse[0] < varia_x and pos_mouse[1] > img_y and pos_mouse[1] < varia_y:
        return True
    return False

def MenuInicial():
    display_surf = pygame.display.set_mode((440, 510), pygame.HWSURFACE)
    pygame.display.set_caption('SNAKE UNI-RN')
    botaoNovoJogo = pygame.image.load("imagens/start.png").convert()
    botaoMuteoff = pygame.image.load("imagens/muteoff.png").convert()
    botaoMuteon = pygame.image.load("imagens/muteon.png").convert()
    botaoExit = pygame.image.load("imagens/exit.png").convert()

    fundo = pygame.image.load("imagens/fundo.png").convert()

    posBotaoNovoJogo = (148, 444)
    posBotaoMuteoff = (366, 12)
    posBotaoMuteon = (366, 76)
    posBotaoExit = (331, 449)
    muteonoff = 0
    score = 0
    recorde = 0


    pygame.init()

    while True:
        if score > recorde:
            recorde = score
        for event in pygame.event.get():
            if event.type == QUIT:
                developers()
                exit()

        xy = pygame.mouse.get_pos()  # retorna a posicao do mouse

        display_surf.blit(fundo, (0, 0))

        fonte = pygame.font.Font(None,36)
        texto = fonte.render(str(recorde), 1, (200, 200, 200))
        textpos = texto.get_rect()
        textpos.left = 55
        textpos.top = 35
        display_surf.blit(texto, textpos)
        #Função Mute
        if muteonoff == 0:
            display_surf.blit(botaoMuteon, posBotaoMuteon)
        if muteonoff == 1:
            display_surf.blit(botaoMuteoff, posBotaoMuteoff)
        if verificaMouse(botaoNovoJogo, posBotaoNovoJogo, xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                clique.play()
                score = iniciar()
            pass
        if verificaMouse(botaoMuteon, posBotaoMuteon, xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pygame.mixer.music.stop()
                clique.play()
                muteonoff = 1
        if verificaMouse(botaoMuteoff, posBotaoMuteoff, xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pygame.mixer.music.play()
                clique.play()
                muteonoff = 0
        if verificaMouse(botaoExit, posBotaoExit, xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                developers()
                exit()

        pygame.display.flip()



def iniciar():
    # Cores
    AZUL = (0, 0, 255)



    # Tamanho da janela
    COMPRIMENTOJANELA = 440
    ALTURAJANELA = 510

    # Direccoes
    CIMA = 8
    BAIXO = 2
    ESQUERDA = 4
    DIREITA = 6

    # Bloco (unidade de tamanho)
    bloco = [18, 18]

    # Quadrado
    # funcao rect(X, Y, largura, altura)
    # Snake
    snake = [[30, 120], [10, 120]]

    cabeca = [30, 120]

    x = randint(0, 20)
    y = randint(0, 19)

    comida = 0
    while True:
        x1 = randint(0, 20)
        y1 = randint(0, 17)
        comidaXY = [int(x1 * 20) + 10, int(y1 * 20) + 120]
        if snake.count(comidaXY) == 0:
            comida = 1
            break

    # Direcçao
    direccao = DIREITA

    morto = 0

    pontos = 0

    # Cria o objecto BACKGROUND
    fundoJanela = pygame.display.set_mode((COMPRIMENTOJANELA, ALTURAJANELA), pygame.HWSURFACE)
    fundodojogo = pygame.image.load("imagens/fundojogo.png").convert()


    # Caption da janela
    pygame.display.set_caption('SNAKE UNI-RN')

    # set up
    pygame.init()
    mainClock = pygame.time.Clock()

    while not morto:
        fundoJanela.blit(fundodojogo, (0, 0))
        # Vemos se o evento QUIT ocorreu
        for event in pygame.event.get():
            if event.type == QUIT:
                developers()
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                # Verifica as mudanças de direcçao validas
                if ((event.key == K_LEFT or event.key == ord('o'))
                        and direccao != DIREITA):
                    direccao = ESQUERDA
                elif ((event.key == K_RIGHT or event.key == ord('p'))
                      and direccao != ESQUERDA):
                    direccao = DIREITA
                elif ((event.key == K_UP or event.key == ord('q'))
                      and direccao != BAIXO):
                    direccao = CIMA
                elif ((event.key == K_DOWN or event.key == ord('a'))
                      and direccao != CIMA):
                    direccao = BAIXO

            # <ESC> para sair do jogo
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Calcular o movimento da cabeca
        if direccao == DIREITA:
            cabeca[0] += 20
            if cabeca[0] > COMPRIMENTOJANELA - 20:
                derrota.play()
                morto = 1
                gameover()


        elif direccao == ESQUERDA:
            cabeca[0] -= 20
            if cabeca[0] < 10:
                derrota.play()
                morto = 1
                gameover()
        elif direccao == CIMA:
            cabeca[1] -= 20
            if cabeca[1] < 110:
                derrota.play()
                morto = 1
                gameover()
        elif direccao == BAIXO:
            cabeca[1] += 20
            if cabeca[1] > ALTURAJANELA - 30:
                derrota.play()
                morto = 1
                gameover()
        # Se estamos a comer alguma parte do corpo morremos
        if snake.count(cabeca) > 0:
            derrota.play()
            morto = 1
            gameover()

        # Cria nova maca fora do corpo da serpente
        if comida == 0:
            while True:
                x1 = randint(0, 20)
                y1 = randint(0, 17)
                comidaXY = [int(x1 * 20) + 10, int(y1 * 20) + 120]
                if snake.count(comidaXY) == 0:
                    comida = 1
                    break

        # Insere a cabeca
        snake.insert(0, list(cabeca))

        # Se a cabeca tiver as mms coordenadas que a comida entao...
        if cabeca[0] == comidaXY[0] and cabeca[1] == comidaXY[1]:
            comeu.play()
            comida = 0
            pontos += 5
        else:
            # remove a cauda
            snake.pop()

        # preenche o fundo
        #fundoJanela.fill(PRETO)

        # Fundo scoreboard
        pygame.draw.rect(fundoJanela, (0,0,0), Rect([10, 18], [420, 100]), 3)

        # Texto
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(pontos), 1, (200, 200, 200))
        textpos = text.get_rect()
        textpos.left = 75
        textpos.top = 45
        fundoJanela.blit(text, textpos)

        # Fundo jogo
        pygame.draw.rect(fundoJanela, (0,0,0), Rect([10, 120], [420, 380]), 3)

        # desenha a serpente
        for x in snake:
            pygame.draw.rect(fundoJanela, AZUL, Rect(x, bloco))

        # desenha a comida
        pygame.draw.rect(fundoJanela, (100, 100, 100), Rect(comidaXY, bloco))

        # desenha os objectos no ecra
        pygame.display.update()
        mainClock.tick(9)  # FPS
    return pontos

def gameover():
    COMPRIMENTOJANELA = 440
    ALTURAJANELA = 510
    running = True
    fundoJanela = pygame.display.set_mode((COMPRIMENTOJANELA, ALTURAJANELA), pygame.HWSURFACE)
    fundodojogo = pygame.image.load("imagens/GAMEOVER.png").convert()
    pygame.display.set_caption('SNAKE UNI-RN')
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                developers()
                pygame.quit()
                sys.exit()
        fundoJanela.blit(fundodojogo, (0, 0))
        pygame.display.update()
        time.sleep(3)
        running = False
def developers():
    print(__BY__)
    print(__VER__)

MenuInicial()

