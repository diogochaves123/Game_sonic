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
    