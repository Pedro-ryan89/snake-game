import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

largura = 1080
altura = 1300


x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade =  10
x_controle = velocidade
y_controle = 0



texto =pygame.font.SysFont('arial',40,True,True)

x_maca= randint(500,1065)
y_maca = randint(1000,1300)

pontos = 0
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
lista_cobra = []
comp_inicial = 5
faleceu = False


def cresce_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],40,50))
 
def reiniciar_jogo():
    global pontos,comp_inicial,x_cobra,y_cobra,lista_cobra,lista_cabeca,x_maca,y_maca,faleceu
    pontos = 0
    comp_inicial = 5
    x_cobra = int(largura/4)
    y_cobra = int(altura/4)
    lista_cobra = []
    lista_cabeca = []
    x_maca= randint(400,1015)
    y_maca = randint(500,950)
    faleceu = False
    

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f"pontos: {pontos}"
    text_tela = texto.render(mensagem,True,(0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()           
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle =  - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else: 
                    y_controle =  - velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle =  velocidade
                    x_controle = 0
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle                
    cobra= pygame.draw.rect(tela,(0,255,0), (x_cobra,y_cobra,40,50 ))
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,40,50))
    if cobra.colliderect(maca):
            y_maca =randint(400,1015)
            x_maca =randint(500,950)
            pontos = pontos + 1
            comp_inicial = comp_inicial + 1
            
           
           
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 1:
        game_over = pygame.font.SysFont('arial',35,True,True)
        mensagem =  'fim de jogo! pressione R para recomeçar'
        texto_formatado = game_over.render(mensagem,True,(0,0,0))
        ret_texto = texto_formatado.get_rect()
        faleceu = True
        while faleceu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                         reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado,(ret_texto))            
            pygame.display.update()
    if x_cobra > largura:
        x_cobra = 0
    elif x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    elif y_cobra > altura:
        y_cobra = 0
        
    
    if len(lista_cobra) > comp_inicial:
        del lista_cobra[0]
        
    
    cresce_cobra(lista_cobra)  
     
    tela.blit(text_tela,(450,40))     
    pygame.display.update() 