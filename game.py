import pygame, random 
pygame.init()

jogadores = str(input(" Insira seu nome: "))
with open('saida.txt','w') as f:
    for passw in jogadores:
        f.write('{}'.format(passw))

jogadores2 = str(input(" Insira seu email: "))
with open('saida2.txt','w') as f:
    for passw in jogadores2:
        f.write('{}'.format(passw))

largura = 960
altura = 672
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Sonic")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("imagens/icone.ico")
pygameDisplay.set_icon(gameIcon)
bg = pygame.image.load("imagens/background.png")
bg_destroy = pygame.image.load("imagens/background.png")
somMorte = pygame.mixer.Sound("sounds/purr.wav")
somMorte.set_volume(0.5)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event

jogando = True
velocidade = 1
def dead(pontos):
    gameDisplay.blit(bg_destroy, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(somMorte)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                        " pontos!", True, black)
    textoContinue = fonteContinue.render(
        "Press enter to continue...", True, white)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()
    return(pontos)

def jogo():
    posicaoX = random.randrange(0, largura)
    posicaoY = 0
    direcao = True
    direcaoSonic = True
    velocidade = 1
    posicaoXSonic = 430
    posicaoYSonic = 550
    movimentoXSonic = 0
    movimentoYSonic = 0
    pontos = 0
    fogo = pygame.image.load("imagens/fogo.png")
    sonic = pygame.image.load("imagens/sonic.png")
    pygame.mixer.music.load("sounds/sonicc.mpeg")
    pygame.mixer.music.play(-5)
    pygame.mixer.music.set_volume(0.2)

    somFogo = pygame.mixer.Sound("sounds/fogoo.mpeg")
    somFogo.set_volume(1)
    pygame.mixer.Sound.play(somFogo)

    alturaSonic = 75
    larguraSonic = 105
    alturaFogo = 26
    larguraFogo = 75
    dificuldade = 29
    jogando = True
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXSonic = - 10
                    sonic = pygame.transform.flip(sonic, True, False)
                    direcaoSonic = False
                elif event.key == pygame.K_RIGHT:
                    movimentoXSonic = 10
                    sonic = pygame.transform.flip(sonic, True, False)
                    direcaoSonic = True
                elif event.key == pygame.K_UP:
                    movimentoYNave = -10
                elif event.key == pygame.K_DOWN:
                    movimentoYNave = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movimentoXSonic = 0
                    movimentoYSonic = 0
        if jogando == True:
            posicaoXSonic = posicaoXSonic + movimentoXSonic
            posicaoYSonic = posicaoYSonic + movimentoYSonic
            if posicaoXSonic < 0:
                posicaoXSonic = 0
            elif posicaoXSonic >= largura - larguraSonic:
                posicaoXSonic = largura - larguraSonic
            if posicaoYSonic < 0:
                posicaoYSonic = 0
            elif posicaoYSonic >= altura - alturaSonic:
                posicaoYSonic = altura - alturaSonic
            gameDisplay.blit(bg, (0, 0))
            if direcao == True:
                if posicaoY < largura-150:
                    posicaoY = posicaoY + velocidade
                else:
                    pygame.mixer.Sound.play(somFogo)
                    direcao = False
                    posicaoX = random.randrange(0, (largura))
                    velocidade = velocidade + 1
                    pontos = pontos + 1
            else:
                if posicaoY >= 0:
                    posicaoY = posicaoY - velocidade
                elif posicaoY >= 0:
                    pygame.mixer.Sound.play(somFogo)
                    direcao = True
                    posicaoX = random.randrange(0, largura)
                    velocidade = velocidade + 1
            if posicaoY > altura:
                posicaoX = random.randrange(0, largura)
                posicaoY = -10
                pontos = pontos + 1
                velocidade = velocidade + 1