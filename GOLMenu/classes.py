"""
Ce script contient toutes les définitions de variables et de classes qui seront
appelées par le script principal
"""
from jeudelavie import*
from constantes import*
from pygame.locals import *
import pygame
import sys

def load_accueil(x):
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))
    #Chargement titre
    titre = pygame.image.load(image_titre_accueil).convert_alpha()
    fenetre.blit(titre,(140,20))
    #Chargement Play
    play = pygame.image.load(image_play_accueil).convert_alpha()
    fenetre.blit(play, (50,200))
    #Chargement Settings
    settings = pygame.image.load(image_settings_accueil).convert_alpha()
    fenetre.blit(settings, (45,280))
    pygame.display.flip()

def load_settings(x):
     #Chargement de la page d'accueil
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
    pygale.display.flip()

def anim_play(x):
    play_click = pygame.image.load(image_play_accueil_click).convert_alpha()
    son_click_titre = pygame.mixer.Sound(son_click)
    son_click_titre.play()
    fenetre.blit(play_click, (50,200))
    continuer_accueil = 0 #Boucle inactive
    continuer_settings = 1 #Activation de la boucle settings
    pygame.display.flip()

def anim_settings(x):
    settings_click = pygame.image.load(image_settings_accueil_click).convert_alpha()
    son_click_titre = pygame.mixer.Sound(son_click)
    son_click_titre.play()
    fenetre.blit(settings_click, (45,280))
    continuer_accueil = 0 #Boucle inactive
    continuer_settings = 1 #Activation de la boucle settings
    pygame.display.flip()






















