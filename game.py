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
