"""
Interface du Jeu de la vie
Ce script a pour but d'afficher l'écran d'accueil interactif du jeu de la vie
Mais également de lancer la simulation du jeu de la vie et de régler certains
paramètres tout en y ajoutant quelques effets pour donner une âme au programme

"""
import pygame, sys
from pygame.locals import *
from constantes import *
from classes import *


pygame.init()
#Initialisation fenêtre
fenetre = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))
#Icone de la fenêtre
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)


continuer_accueil = True #Boucle active
continuer_settings = False #Boucle inactive
continuer_play = 0 #Boucle inactivePP
sound = 1


while True:

    if sound == 1:
        music_fond = pygame.mixer.music.load(bande_son)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)


    #BOUCLE PAGE D'ACCUEIL
    while continuer_accueil:
        #fond
        accueil = pygame.image.load(image_accueil).convert()
        fenetre.blit(accueil, (0,0))
        #titre
        titre = pygame.image.load(image_titre_accueil).convert_alpha()
        fenetre.blit(titre,(140,20))
        #Play
        play = pygame.image.load(image_play_accueil).convert_alpha()
        fenetre.blit(play, (50,200))
        #Settings
        settings = pygame.image.load(image_settings_accueil).convert_alpha()
        fenetre.blit(settings, (45,280))
        pygame.display.flip()


        for event in pygame.event.get():

            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #Detection clic sur les titres:
            if event.type == MOUSEBUTTONDOWN:
                #Clic sur PLAY
                if 50 < event.pos[0] < 312 and 200 < event.pos[1] < 267:
                    play_click = pygame.image.load(image_play_accueil_click).convert_alpha()
                    son_click_titre = pygame.mixer.Sound(son_click)
                    son_click_titre.play()
                    fenetre.blit(play_click, (50,200))
                #Clic sur Settings
                if 45 < event.pos[0] < 512 and 280 < event.pos[1] < 348 :
                    settings_click = pygame.image.load(image_settings_accueil_click).convert_alpha()
                    son_click_titre = pygame.mixer.Sound(son_click)
                    son_click_titre.play()
                    fenetre.blit(settings_click, (45,280))
                    continuer_accueil = False #Boucle inactive
                    continuer_settings = True #Activation de la boucle settings
            pygame.display.flip()


    #BOUCLE SETTINGS
    while continuer_settings:
        #event souris
        for event in pygame.event.get():

            #Fermeture programme
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            #Test selection de couleur
            if event.type == MOUSEBUTTONDOWN:
                #Bleu
                if event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 200 and event.pos[0] < 250:
                    color_select = BLUE
                #Cyan
                elif event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 260 and event.pos[0] < 310:
                    color_select = CYAN
                #Jaune
                elif event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 320 and event.pos[0] < 370:
                    color_select = YELLOW
                #Magenta
                elif event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 380 and event.pos[0] < 430:
                    color_select = MAGENTA
                #Orange
                elif event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 440 and event.pos[0] < 490:
                    color_select = ORANGE
                #Rouge
                elif event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 500 and event.pos[0] < 550:
                    color_select = RED
                #Vert
                elif event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 560 and event.pos[0] < 610:
                    color_select = GREEN
                #Violet
                elif event.pos[1] > 25 and event.pos[1] < 75 and event.pos[0] > 620 and event.pos[0] < 670:
                    color_select = PURPLE

            #sortir de la page
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_settings = False
                continuer_accueil = True


        #Chargement du fond
        accueil = pygame.image.load(image_accueil).convert()
        fenetre.blit(accueil, (0,0))
        #Chargement titre couleur
        settings_couleur = pygame.image.load(set_couleur).convert_alpha()
        fenetre.blit(settings_couleur, (20,20))
        #Chargement couleurs
        settings_bleu = pygame.image.load(case_bleu).convert()
        fenetre.blit(settings_bleu, (200,25))
        settings_cyan = pygame.image.load(case_cyan).convert()
        fenetre.blit(settings_cyan, (260,25))
        settings_jaune = pygame.image.load(case_jaune).convert()
        fenetre.blit(settings_jaune, (320,25))
        settings_magenta = pygame.image.load(case_magenta).convert()
        fenetre.blit(settings_magenta, (380,25))
        settings_orange = pygame.image.load(case_orange).convert()
        fenetre.blit(settings_orange, (440,25))
        settings_rouge = pygame.image.load(case_rouge).convert()
        fenetre.blit(settings_rouge, (500,25))
        settings_vert = pygame.image.load(case_vert).convert()
        fenetre.blit(settings_vert, (560,25))
        settings_violet = pygame.image.load(case_violet).convert()
        fenetre.blit(settings_violet, (620,25))

        #Importation du carré de sélection des couleurs
        settings_select_frame = pygame.image.load(set_selectframe).convert()



        if color_select == BLUE:
            fenetre.blit(settings_select_frame, (200,75))
            pygame.display.flip()
        elif color_select == CYAN:
            fenetre.blit(settings_select_frame, (260,75))
            pygame.display.flip()
        elif color_select == YELLOW:
            fenetre.blit(settings_select_frame, (320,75))
            pygame.display.flip()
        elif color_select == MAGENTA:
            fenetre.blit(settings_select_frame, (380,75))
            pygame.display.flip()
        elif color_select == ORANGE:
            fenetre.blit(settings_select_frame, (440,75))
            pygame.display.flip()
        elif color_select == GREEN:
            fenetre.blit(settings_select_frame, (560,75))
            pygame.display.flip()
        elif color_select == PURPLE:
            fenetre.blit(settings_select_frame, (620,75))
            pygame.display.flip()
        elif color_select == RED:
            fenetre.blit(settings_select_frame, (500,75))
            pygame.display.flip()

    pygame.display.update()
