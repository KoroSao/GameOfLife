import random, pygame, sys
from pygame.locals import *
from pygame import gfxdraw ##pour dessiner des formes avec anti-aliasing
from math import *
from random import randint

FPS = 1000
FPSEVOLUTION = 15
WINDOWWIDTH =1280
WINDOWHEIGHT = 720
BOXSIZE = 21
GAPSIZE = 1
BOARDWIDTH = 30 # number of columns of icons
BOARDHEIGHT = 30 # number of rows of icons
MARGIN = 30 - GAPSIZE
YMARGINQUADRILLAGE = MARGIN
XMARGINQUADRILLAGE = WINDOWWIDTH - (BOXSIZE+GAPSIZE)*BOARDWIDTH + GAPSIZE - YMARGINQUADRILLAGE - 200
GRIDWIDTH = (BOXSIZE+GAPSIZE)*BOARDWIDTH + GAPSIZE
GRIDHEIGHT = (BOXSIZE+GAPSIZE)*BOARDWIDTH + GAPSIZE


TOOLBARHEIGHT = 240
TOOLBARWIDTH = WINDOWWIDTH - (GRIDWIDTH + 3*MARGIN) - 200

INFOHEIGHT = WINDOWHEIGHT - (TOOLBARHEIGHT + 3*MARGIN + GAPSIZE)
INFOWIDTH = TOOLBARWIDTH

SMALLMARGIN = 15
TOOLBOXWIDTH = int( (TOOLBARWIDTH-4*SMALLMARGIN)/3 )
TOOLBOXHEIGHT = int( (TOOLBARHEIGHT-(SMALLMARGIN*4+25))/2 )

SON = 0 ##valeur initiale du son
R = 0
G = 0
B = 0





#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)

ORANGE   = (255, 150,   0)
YELLOW   = (252, 255,   0)
GREEN    = (  0, 221,  16)
CYAN     = (  0, 212, 250)
BLUE     = ( 53,   0, 250)
PURPLE   = (165,   0, 250)
RED      = (255,   0,   0)
MAGENTA  = (250,   0, 247)
LIGHTGRAY= (230, 230, 230)
LIGHTRED = (255, 90 ,  90)
LIGHTLIGHTRED=(255, 110, 110)
MIDDLEGRAY=(110, 110, 110)
MIDDLELIGHTGRAY= (220, 220, 220)
SEMILIGHTGRAY=(210, 210, 210)

BGCOLOR = LIGHTGRAY
BOXCOLOR = (R, G, B)
TEMPCOLOR = (MIDDLELIGHTGRAY)
EMPTYBOXCOLOR = (255,255,255,0)
BORDERCOLOR = GRAY
sound_value = 0



def main():
    global FPSCLOCK, DISPLAYSURF, BOXCOLOR, TEMPCOLOR, FPSEVOLUTION, BOXSIZE, BOARDWIDTH, BOARDHEIGHT, filledBoxes, tempBoxes, SIZE100, SIZE
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Game of Life :3')
    mainBoard = getBoard()
    filledBoxes = generateBoxesData(False)
    tempBoxes = generateBoxesData(False)

    duck1 = pygame.mixer.Sound("sons/duck1.wav")
    duck2 = pygame.mixer.Sound("sons/duck2.wav")
    duck3 = pygame.mixer.Sound("sons/duck3.wav")

    bulle1 = pygame.mixer.Sound("sons/bulle1.wav")
    bulle2 = pygame.mixer.Sound("sons/bulle2.wav")
    bulle3 = pygame.mixer.Sound("sons/bulle3.wav")

    eraser1 = pygame.mixer.Sound("sons/eraser1.wav")
    eraser2 = pygame.mixer.Sound("sons/eraser2.wav")
    eraser3 = pygame.mixer.Sound("sons/eraser3.wav")

    Snarehit = pygame.mixer.Sound("sons/Snarehit.wav")
    Lowdrum = pygame.mixer.Sound("sons/LowDrum.wav")
    Highdrum = pygame.mixer.Sound("sons/HighDrum.wav")

    Funky = pygame.mixer.music.load("sons/Funky.wav")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.1)

    Waitaminute = pygame.mixer.Sound("sons/Waitaminute.wav")
    Whoareyou = pygame.mixer.Sound("sons/Whoareyou.wav")
    Wow = pygame.mixer.Sound("sons/wow.wav")
    mouseClicked = False
    filling = False
    unfilling = False
    evoluting = False
    CLEARBUTTON = False
    EVOLUTIONCLICKED = False

    movingcircleSON = False
    SONmoving = False
    SON100=0

    movingcircleR = False
    Rmoving = False
    R100=86

    movingcircleG = False
    Gmoving = False
    G100 = 20

    movingcircleB = False
    Bmoving = False
    B100 = 73

    movingcircleFRAME = False
    FRAMEmoving = False
    FRAME100 = 30

    movingcircleSIZE = False
    SIZEmoving = False
    SIZE100 = 53

    RGBWave = True

    canontemp = False

##==============================================================================









                               #BOUCLE DE JEU#
    while True:

##==============================================================================
##Dessin de l'interface

        ##fond
        DISPLAYSURF.fill(BGCOLOR)

        ##contour de la barre d'outils
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN, WINDOWHEIGHT-(MARGIN+TOOLBARHEIGHT), TOOLBARWIDTH, TOOLBARHEIGHT-2), GAPSIZE)
        ##titre outils
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN+40, WINDOWHEIGHT-(MARGIN+TOOLBARHEIGHT-SMALLMARGIN), TOOLBARWIDTH-2*40, 25), GAPSIZE)
        ##cadre son
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN+SMALLMARGIN, WINDOWHEIGHT-(TOOLBARHEIGHT+MARGIN-2*SMALLMARGIN-25), TOOLBOXWIDTH, TOOLBOXHEIGHT), GAPSIZE)
        ##cadre couleur
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN+2*SMALLMARGIN+(TOOLBARWIDTH-4*SMALLMARGIN)/3, WINDOWHEIGHT-(TOOLBARHEIGHT+MARGIN-2*SMALLMARGIN-25), TOOLBOXWIDTH, TOOLBOXHEIGHT), GAPSIZE)
        ##cadre taille
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN+3*SMALLMARGIN+2*(TOOLBARWIDTH-4*SMALLMARGIN)/3, WINDOWHEIGHT-(TOOLBARHEIGHT+MARGIN-2*SMALLMARGIN-25), TOOLBOXWIDTH, TOOLBOXHEIGHT), GAPSIZE)
        ##cadre structures
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN+SMALLMARGIN, WINDOWHEIGHT-(MARGIN+TOOLBARHEIGHT) + 3*SMALLMARGIN + 25 + (TOOLBARHEIGHT-(SMALLMARGIN*4+25))/2, TOOLBARWIDTH-2*SMALLMARGIN, TOOLBOXHEIGHT), GAPSIZE)


        ##contour de la barre d'infos
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN, MARGIN, INFOWIDTH, INFOHEIGHT), GAPSIZE)
        ##titre infos
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN+40, MARGIN+SMALLMARGIN, INFOWIDTH-2*40, 25), GAPSIZE)
        ##cadre infos
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (MARGIN+SMALLMARGIN, MARGIN+2*SMALLMARGIN+25, INFOWIDTH-2*SMALLMARGIN, INFOHEIGHT-(3*SMALLMARGIN+25)), GAPSIZE)

        ##fond de la grille
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGINQUADRILLAGE-GAPSIZE, YMARGINQUADRILLAGE-GAPSIZE, GRIDWIDTH, GRIDHEIGHT))
        ##dessin des cases
        drawBoard(0, filledBoxes, BOXCOLOR)
        drawBoard(1, tempBoxes, TEMPCOLOR)



##==============================================================================

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                boxx, boxy = getBoxAtPixel(mousex, mousey)
                if canontemp:
                    if boxx != None and boxy != None:
                        tempBoxes = generateBoxesData(False)
                        tempBoxes = generate_structure_Canon(1, boxx, boxy, 1)

            elif event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                mouseClicked = True
                SONmoving = True
                Rmoving = True
                Gmoving = True
                Bmoving = True
                FRAMEmoving = True
                SIZEmoving = True
                print("x=", mousex, "y=", mousey)
                if canontemp:
                    if boxx != None and boxy != None:
                        filledBoxes = generate_structure_Canon(0, boxx, boxy, 1)
                    canontemp = False
                    tempBoxes = generateBoxesData(False)



            elif event.type == MOUSEBUTTONUP:
                mouseClicked = False
                filling = False
                unfilling = False
                SONmoving = False
                Rmoving = False
                Gmoving = False
                Bmoving = False
                FRAMEmoving = False
                SIZEmoving = False
                if CLEARBUTTON == True:
                    Snarehit.play()
                    CLEARBUTTON = False
                    filledBoxes = generateBoxesData(False)
                if 27<mousex<37 and 27<mousey<37:
                    Waitaminute.play()
                if 27<mousex<37 and 680<mousey<690:
                    Whoareyou.play()
                if 352<mousex<362 and 450<mousey<460:
                    Wow.play()
                EVOLUTIONCLICKED = False

            elif event.type == KEYDOWN:

                if event.key == K_SPACE:
                    evoluting = True
                    print("evoluting")

                if event.key == K_c:
                    if boxx != None and boxy != None:
                        filledBoxes = generate_structure_Canon(0, boxx, boxy, 1)
                        pygame.font.init()
                        font_console = pygame.font.SysFont('microsoftyaheimicrosoftyaheiui', 12, BORDERCOLOR)
                        text_console_canon = font_console.render('{0}'.format("Canon has been generated"), True, BORDERCOLOR, BGCOLOR)
                        DISPLAYSURF.blit(text_console_canon,(100, 100))

                if event.key == K_v:

                    if not canontemp:
                        canontemp = True


                if event.key == K_f:
                    filledBoxes = generateBoxesData(False)
                    generate_structure_Frame(1)

                if event.key == K_d:
                    filledBoxes = generateBoxesData(False)
                    generate_structure_demo(1)

            elif event.type == KEYUP:
                if event.key == K_SPACE:
                    evoluting = False
                    print("notevoluting")

        if SONmoving:
            SON100, movingcircleSON = drawCursor(mousex, mousey, 70, 520, 550, SON100, movingcircleSON, True)
        else:
            SON100, movingcircleSON = drawCursor(mousex, mousey, 70, 520, 550, SON100, False, False)

        if FRAMEmoving:
            FRAME100, movingcircleFRAME = drawCursor(mousex, mousey, 281, 520, 550, FRAME100, movingcircleFRAME, True)
        else:
            FRAME100, movingcircleFRAME = drawCursor(mousex, mousey, 281, 520, 550, FRAME100, False, False)

        if SIZEmoving:
            SIZE100, movingcircleSIZE = drawCursor(mousex, mousey, 320, 520, 550, SIZE100, movingcircleSIZE, True)
        else:
            SIZE100, movingcircleSIZE = drawCursor(mousex, mousey, 320, 520, 550, SIZE100, False, False)

        if Rmoving:
            R100, movingcircleR = drawCursor(mousex, mousey, 160, 520, 550, R100, movingcircleR, True)
        else :
            R100, movingcircleR = drawCursor(mousex, mousey, 160, 520, 550, R100, False, False)

        if Gmoving:
            G100, movingcircleG = drawCursor(mousex, mousey, 190, 520, 550, G100, movingcircleG, True)
        else :
            G100, movingcircleG = drawCursor(mousex, mousey, 190, 520, 550, G100, False, False)

        if Bmoving:
            B100, movingcircleB = drawCursor(mousex, mousey, 220, 520, 550, B100, movingcircleB, True)
        else:
            B100, movingcircleB = drawCursor(mousex, mousey, 220, 520, 550, B100, False, False)
                ##(mousex, mousey, X, HAUTDURECTANGLE, BASDURECTANGLE, VALEUR, movingcircleVALEUR, clickedcircle)

##==============================================================================

        if FRAME100 != 0 :
            FPSEVOLUTION = int(3+0.25*FRAME100)
        else:
            FPSEVOLUTION = 3



        R = int(R100*2.55)
        G = int(G100 * 2.55)
        B = int(B100 * 2.55)
        BOXCOLOR = (R,G,B)



        SIZE = int( SIZE100*96/100 +4 )
        BOARDHEIGHT = SIZE
        BOARDWIDTH = SIZE

        BOXSIZE = ( GRIDHEIGHT - (SIZE+1)*GAPSIZE )/SIZE

##==============================================================================
##RGB STYLE
        if RGBWave == True:
            RUP = True
            RDOWN = False
            if RUP == True:
                R =+ 1
                if R == 255:
                    RUP = False
                    RDOWN = True
            elif RDOWN ==True:
                R =-1
                if R == 0:
                    RDOWN = False
                    RUP = True

##==============================================================================
##Bouton de réinitialisation


        if mouseClicked and WINDOWWIDTH-115-70 < mousex < WINDOWWIDTH-115+70 and MARGIN < mousey < MARGIN+70+70:
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 65, 65, MIDDLEGRAY)
            pygame.gfxdraw.aaellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 65, 65, MIDDLEGRAY)
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 62, 62, LIGHTLIGHTRED)
            pygame.gfxdraw.aaellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 62, 62, LIGHTLIGHTRED)
            CLEARBUTTON = True



        else:
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 70, 70, GRAY)
            pygame.gfxdraw.aaellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 70, 70, GRAY)
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 67, 67, LIGHTRED)
            pygame.gfxdraw.aaellipse(DISPLAYSURF, WINDOWWIDTH-115, 70+MARGIN, 67, 67, LIGHTRED)

##==============================================================================
##Bouton d'évolution

        if mouseClicked and WINDOWWIDTH-115-70 < mousex < WINDOWWIDTH-115+70 and WINDOWHEIGHT-MARGIN > mousey > WINDOWHEIGHT-(MARGIN+70+70) and not evoluting and not EVOLUTIONCLICKED:
            evoluting = True
            EVOLUTIONCLICKED = True
            Lowdrum.play()
        elif mouseClicked and WINDOWWIDTH-115-70 < mousex < WINDOWWIDTH-115+70 and WINDOWHEIGHT-MARGIN > mousey > WINDOWHEIGHT-(MARGIN+70+70) and evoluting and not EVOLUTIONCLICKED:
            evoluting = False
            EVOLUTIONCLICKED = True
            Highdrum.play()

        if evoluting:
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, WINDOWHEIGHT-(70+MARGIN), 65, 65, MIDDLEGRAY)
            pygame.gfxdraw.aaellipse(DISPLAYSURF, WINDOWWIDTH-115, WINDOWHEIGHT-(70+MARGIN), 65, 65, MIDDLEGRAY)
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, WINDOWHEIGHT-(70+MARGIN), 62, 62, SEMILIGHTGRAY)
            pygame.gfxdraw.aaellipse(DISPLAYSURF, WINDOWWIDTH-115, WINDOWHEIGHT-(70+MARGIN), 62, 62, SEMILIGHTGRAY)
        else:
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, WINDOWHEIGHT-(70+MARGIN), 70, 70, GRAY)
            pygame.gfxdraw.aaellipse(DISPLAYSURF, WINDOWWIDTH-115, WINDOWHEIGHT-(70+MARGIN), 70, 70, GRAY)
            pygame.gfxdraw.filled_ellipse(DISPLAYSURF, WINDOWWIDTH-115, WINDOWHEIGHT-(70+MARGIN), 67, 67, BOXCOLOR)

##==============================================================================
##Remplir/effacer une case
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            ##La souris est au dessus d'une case
            if not filledBoxes[boxx][boxy] and mouseClicked and not unfilling:
                filledBoxes[boxx][boxy] = True 
                filling = True
                sound_value = randint(1,3)
                if R100 == 100 and G100==100 and B100==0:
                    if sound_value == 1:
                        duck1.play()
                    elif sound_value == 2:
                        duck2.play()
                    elif sound_value == 3:
                        duck3.play()
                else:
                    if sound_value == 1:
                        bulle1.play()
                    elif sound_value == 2:
                        bulle2.play()
                    elif sound_value == 3:
                        bulle3.play()


            elif filledBoxes[boxx][boxy] and mouseClicked and not filling:
                filledBoxes[boxx][boxy] = False 
                unfilling = True
                if sound_value == 1:
                    eraser1.play()
                elif sound_value == 2:
                    eraser2.play()
                elif sound_value == 3:
                    eraser3.play()
##==============================================================================
##Evolution
        if evoluting:
            evolution(filledBoxes)
            FPSCLOCK.tick(FPSEVOLUTION)
            pygame.mixer.music.set_volume(1)

        elif not evoluting:
            pygame.mixer.music.set_volume(0.5)
##==============================================================================

        print (mousex, mousey)

        pygame.display.update()
        FPSCLOCK.tick(FPS)
##==============================================================================








                                 #FONCTIONS#

##==============================================================================
##Curseur
def drawCursor(mousex, mousey, X, HAUTDURECTANGLE, BASDURECTANGLE, VALEUR, movingcircle, clickedcircle):

    CIRCLEY = int( BASDURECTANGLE-(VALEUR*((BASDURECTANGLE-HAUTDURECTANGLE)/100)) )

    if clickedcircle:
        if sqrt( (mousex-X)*(mousex-X) + (mousey-CIRCLEY)*(mousey-CIRCLEY) ) < 10 or (HAUTDURECTANGLE-3 < mousey < BASDURECTANGLE+3 and X-5 < mousex < X+5):
            movingcircle = True


    if movingcircle:
        if HAUTDURECTANGLE < mousey < BASDURECTANGLE:
            CIRCLEY = mousey
        elif mousey > BASDURECTANGLE:
            CIRCLEY = BASDURECTANGLE
        elif mousey < HAUTDURECTANGLE:
            CIRCLEY = HAUTDURECTANGLE

    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (X-5, HAUTDURECTANGLE, 11, BASDURECTANGLE-HAUTDURECTANGLE), 0)
    pygame.gfxdraw.filled_ellipse(DISPLAYSURF,X, HAUTDURECTANGLE, 5, 5, BORDERCOLOR)
    pygame.gfxdraw.aaellipse(DISPLAYSURF, X, HAUTDURECTANGLE, 5, 5, BORDERCOLOR)

    pygame.gfxdraw.filled_ellipse(DISPLAYSURF, X, BASDURECTANGLE, 5, 5, BORDERCOLOR)
    pygame.gfxdraw.aaellipse(DISPLAYSURF, X, BASDURECTANGLE, 5, 5, BORDERCOLOR)

    pygame.draw.rect(DISPLAYSURF, WHITE, (X-4, HAUTDURECTANGLE, 9, BASDURECTANGLE-HAUTDURECTANGLE), 0)
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (X-4, CIRCLEY, 9, BASDURECTANGLE-CIRCLEY), )

    pygame.gfxdraw.filled_ellipse(DISPLAYSURF, X, HAUTDURECTANGLE, 4, 4, WHITE)
    pygame.gfxdraw.aaellipse(DISPLAYSURF, X, HAUTDURECTANGLE, 4, 4, WHITE)

    pygame.gfxdraw.filled_ellipse(DISPLAYSURF, X, BASDURECTANGLE, 4, 4, BORDERCOLOR)
    pygame.gfxdraw.aaellipse(DISPLAYSURF, X, BASDURECTANGLE, 4, 4, BORDERCOLOR)


    pygame.gfxdraw.filled_ellipse(DISPLAYSURF, X, CIRCLEY, 8, 8, BOXCOLOR)
    pygame.gfxdraw.aaellipse(DISPLAYSURF, X, CIRCLEY, 8, 8, BORDERCOLOR)


    VALEUR = 100*(BASDURECTANGLE-CIRCLEY)/(BASDURECTANGLE-HAUTDURECTANGLE)
    VALEURINT = int(VALEUR)

    pygame.font.init()
    myfont = pygame.font.SysFont('microsoftyaheimicrosoftyaheiui', 12, BORDERCOLOR)
    textsurface = myfont.render('{0}'.format(VALEURINT), True, BORDERCOLOR, BGCOLOR)

    DISPLAYSURF.blit(textsurface,(X+12, CIRCLEY-9))

    return VALEUR, movingcircle

##==============================================================================



##==============================================================================
def drawBoard(x, filled, COLOR):
    # Draws all of the boxes in their empty or filled state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if filled[boxx][boxy]:
                # Draw a filled box.
                pygame.draw.rect(DISPLAYSURF, COLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                if x ==0:
                    pygame.draw.rect(DISPLAYSURF, EMPTYBOXCOLOR, (left, top, BOXSIZE, BOXSIZE))

##==============================================================================



##==============================================================================
def getBoard():
    board=[]
    for x in range(100):
        board.append([0]*100)
    return board
##==============================================================================



##==============================================================================
def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)
##==============================================================================



##==============================================================================
def generateBoxesData(val):
    Boxes = []
    for i in range(100):
        Boxes.append([val] * 100)
    return Boxes
##==============================================================================



##==============================================================================
def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGINQUADRILLAGE
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGINQUADRILLAGE
    return (left, top)
##==============================================================================
def generate_structure_Canon(frame, posx, posy, x):
    print("Canon has been Generated")

    if posx != None:
        posx = int(posx)
        posy = int(posy)


        if frame == 0:


            filledBoxes[posx+1][posy] = True
            filledBoxes[posx][posy+1] = True
            filledBoxes[posx+1][posy+1] = True

            filledBoxes[posx+11][posy-1] = True
            filledBoxes[posx+12][posy-2] = True
            filledBoxes[posx+13][posy-2] = True
            filledBoxes[posx+10][posy] = True
            filledBoxes[posx+10][posy+1] = True
            filledBoxes[posx+10][posy+2] = True
            filledBoxes[posx+11][posy+3] = True
            filledBoxes[posx+12][posy+4] = True
            filledBoxes[posx+13][posy+4] = True

            filledBoxes[posx+14][posy+1] = True

            filledBoxes[posx+15][posy+3] = True
            filledBoxes[posx+16][posy+2] = True
            filledBoxes[posx+16][posy+1] = True
            filledBoxes[posx+16][posy+0] = True
            filledBoxes[posx+17][posy+1] = True #pointe flÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨che
            filledBoxes[posx+15][posy-1] = True

            filledBoxes[posx+20][posy+0] = True
            filledBoxes[posx+20][posy-1] = True
            filledBoxes[posx+20][posy-2] = True
            filledBoxes[posx+21][posy+0] = True
            filledBoxes[posx+21][posy-1] = True
            filledBoxes[posx+21][posy-2] = True
            filledBoxes[posx+22][posy-3] = True
            filledBoxes[posx+24][posy-4] = True
            filledBoxes[posx+24][posy-3] = True
            filledBoxes[posx+22][posy+1] = True
            filledBoxes[posx+24][posy+1] = True
            filledBoxes[posx+24][posy+2] = True

            filledBoxes[posx+34][posy-2] = True
            filledBoxes[posx+35][posy-2] = True
            filledBoxes[posx+34][posy-1] = True
            filledBoxes[posx+35][posy-1] = True
            return filledBoxes

        elif frame == 1:

            tempBoxes[posx][posy] = True
            tempBoxes[posx+1][posy] = True
            tempBoxes[posx][posy+1] = True
            tempBoxes[posx+1][posy+1] = True

            tempBoxes[posx+11][posy-1] = True
            tempBoxes[posx+12][posy-2] = True
            tempBoxes[posx+13][posy-2] = True
            tempBoxes[posx+10][posy] = True
            tempBoxes[posx+10][posy+1] = True
            tempBoxes[posx+10][posy+2] = True
            tempBoxes[posx+11][posy+3] = True
            tempBoxes[posx+12][posy+4] = True
            tempBoxes[posx+13][posy+4] = True

            tempBoxes[posx+14][posy+1] = True

            tempBoxes[posx+15][posy+3] = True
            tempBoxes[posx+16][posy+2] = True
            tempBoxes[posx+16][posy+1] = True
            tempBoxes[posx+16][posy+0] = True
            tempBoxes[posx+17][posy+1] = True #pointe flÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¨che
            tempBoxes[posx+15][posy-1] = True

            tempBoxes[posx+20][posy+0] = True
            tempBoxes[posx+20][posy-1] = True
            tempBoxes[posx+20][posy-2] = True
            tempBoxes[posx+21][posy+0] = True
            tempBoxes[posx+21][posy-1] = True
            tempBoxes[posx+21][posy-2] = True
            tempBoxes[posx+22][posy-3] = True
            tempBoxes[posx+24][posy-4] = True
            tempBoxes[posx+24][posy-3] = True
            tempBoxes[posx+22][posy+1] = True
            tempBoxes[posx+24][posy+1] = True
            tempBoxes[posx+24][posy+2] = True

            tempBoxes[posx+34][posy-2] = True
            tempBoxes[posx+35][posy-2] = True
            tempBoxes[posx+34][posy-1] = True
            tempBoxes[posx+35][posy-1] = True
            return tempBoxes



def generate_structure_Frame(x):
    print("Frame has been Generated")
    for loop in range(55):
        filledBoxes[0][loop] = True
        filledBoxes[loop][0] = True
        filledBoxes[54][loop] = True
        filledBoxes[loop][54] = True

def generate_structure_demo(x):
    #Bloc
    filledBoxes[3][3]=True
    filledBoxes[3][4]=True
    filledBoxes[4][3]=True
    filledBoxes[4][4]=True
    #Tube
    filledBoxes[8][3]=True
    filledBoxes[9][4]=True
    filledBoxes[8][5]=True
    filledBoxes[7][4]=True
    #Bateau
    filledBoxes[12][3]=True
    filledBoxes[13][3]=True
    filledBoxes[12][4]=True
    filledBoxes[13][5]=True
    filledBoxes[14][4]=True
    #Navire
    filledBoxes[17][3]=True
    filledBoxes[18][3]=True
    filledBoxes[17][4]=True
    filledBoxes[18][5]=True
    filledBoxes[19][4]=True
    filledBoxes[19][5]=True
    #Serpent
    filledBoxes[22][3]=True
    filledBoxes[22][4]=True
    filledBoxes[23][3]=True
    filledBoxes[24][4]=True
    filledBoxes[25][4]=True
    filledBoxes[25][3]=True
    #Barge
    filledBoxes[28][4]=True
    filledBoxes[29][3]=True
    filledBoxes[29][5]=True
    filledBoxes[30][4]=True
    filledBoxes[30][2]=True
    filledBoxes[31][3]=True
    #Porte-Avion
    filledBoxes[34][4]=True
    filledBoxes[34][5]=True
    filledBoxes[35][5]=True
    filledBoxes[37][3]=True
    filledBoxes[36][3]=True
    filledBoxes[37][4]=True
    #Ruche
    filledBoxes[40][3]=True
    filledBoxes[40][4]=True
    filledBoxes[41][2]=True
    filledBoxes[42][3]=True
    filledBoxes[42][4]=True
    filledBoxes[41][5]=True
    #Miche de pain
    filledBoxes[45][3]=True
    filledBoxes[45][4]=True
    filledBoxes[46][5]=True
    filledBoxes[47][4]=True
    filledBoxes[48][3]=True
    filledBoxes[46][2]=True
    filledBoxes[47][2]=True
    #HameÃƒÂ§on
    filledBoxes[3][8]=True
    filledBoxes[4][8]=True
    filledBoxes[4][9]=True
    filledBoxes[4][10]=True
    filledBoxes[5][11]=True
    filledBoxes[6][11]=True
    filledBoxes[6][10]=True
    #CanoÃƒÂ«
    filledBoxes[9][8]=True
    filledBoxes[10][8]=True
    filledBoxes[9][9]=True
    filledBoxes[10][10]=True
    filledBoxes[11][11]=True
    filledBoxes[12][12]=True
    filledBoxes[13][12]=True
    filledBoxes[13][11]=True
    #Longue Barge
    filledBoxes[16][11]=True
    filledBoxes[17][10]=True
    filledBoxes[18][9]=True
    filledBoxes[19][8]=True
    filledBoxes[17][12]=True
    filledBoxes[18][11]=True
    filledBoxes[19][10]=True
    filledBoxes[20][9]=True
    #Long Navire
    filledBoxes[23][11]=True
    filledBoxes[23][10]=True
    filledBoxes[24][9]=True
    filledBoxes[25][8]=True
    filledBoxes[24][11]=True
    filledBoxes[25][10]=True
    filledBoxes[26][9]=True
    filledBoxes[26][8]=True
    #Mare
    filledBoxes[30][8]=True
    filledBoxes[31][8]=True
    filledBoxes[30][11]=True
    filledBoxes[31][11]=True
    filledBoxes[30][8]=True
    filledBoxes[29][9]=True
    filledBoxes[29][10]=True
    filledBoxes[32][9]=True
    filledBoxes[32][10]=True
    #Long CanoÃƒÂ«
    filledBoxes[35][8]=True
    filledBoxes[36][8]=True
    filledBoxes[35][9]=True
    filledBoxes[36][10]=True
    filledBoxes[37][11]=True
    filledBoxes[38][12]=True
    filledBoxes[39][13]=True
    filledBoxes[40][13]=True
    filledBoxes[40][12]=True
    #Double HameÃƒÂ§on 2
    filledBoxes[43][13]=True
    filledBoxes[44][13]=True
    filledBoxes[43][12]=True
    filledBoxes[44][11]=True
    filledBoxes[45][11]=True
    filledBoxes[46][11]=True
    filledBoxes[46][10]=True
    filledBoxes[46][9]=True
    filledBoxes[47][8]=True
    filledBoxes[48][8]=True
    filledBoxes[48][9]=True
    #Mangeur Type 2
    filledBoxes[5][17]=True
    filledBoxes[4][18]=True
    filledBoxes[4][19]=True
    filledBoxes[4][20]=True
    filledBoxes[3][20]=True
    filledBoxes[6][18]=True
    filledBoxes[6][19]=True
    filledBoxes[6][20]=True
    filledBoxes[7][20]=True
    filledBoxes[8][20]=True
    filledBoxes[9][21]=True
    filledBoxes[6][22]=True
    filledBoxes[7][22]=True
    filledBoxes[8][22]=True
    filledBoxes[6][23]=True
    filledBoxes[4][23]=True
    filledBoxes[4][22]=True
    filledBoxes[3][23]=True
    filledBoxes[3][22]=True
    #27 cellules
    filledBoxes[15][17]=True
    filledBoxes[16][17]=True
    filledBoxes[15][18]=True
    filledBoxes[15][19]=True
    filledBoxes[14][20]=True
    filledBoxes[13][20]=True
    filledBoxes[13][19]=True

    filledBoxes[16][20]=True
    filledBoxes[16][21]=True
    filledBoxes[16][22]=True
    filledBoxes[16][23]=True
    filledBoxes[15][23]=True

    filledBoxes[17][20]=True
    filledBoxes[18][21]=True
    filledBoxes[18][22]=True
    filledBoxes[18][23]=True
    filledBoxes[19][23]=True
    filledBoxes[20][23]=True
    filledBoxes[21][24]=True
    filledBoxes[18][25]=True
    filledBoxes[19][25]=True
    filledBoxes[20][25]=True
    filledBoxes[18][26]=True

    filledBoxes[16][26]=True
    filledBoxes[15][26]=True
    filledBoxes[16][25]=True
    filledBoxes[15][25]=True

    #JeSuisClignotant
    filledBoxes[45][40]=True
    filledBoxes[46][40]=True
    filledBoxes[47][40]=True





##==============================================================================
def evolution(filled):
    Tampon = generateBoxesData(0)

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            compte = 0
            if x == 0 or y== 0 or x == BOARDWIDTH-1 or y == BOARDHEIGHT-1:
                Tampon[x][y] = -1

            else:

                if filled[x+1][y]:
                    compte += 1
                if filled[x+1][y+1]:
                    compte += 1
                if filled[x+1][y-1]:
                    compte += 1
                if filled[x][y+1]:
                    compte += 1
                if filled[x][y-1]:
                    compte += 1
                if filled[x-1][y]:
                    compte += 1
                if filled[x-1][y+1]:
                    compte += 1
                if filled[x-1][y-1]:
                    compte += 1

                if filled[x][y]:
                    if compte !=2 and compte!=3:

                        Tampon[x][y] = -1

                if not filled[x][y]:
                    if compte == 3:
                        print(compte)
                        Tampon[x][y] = 2
    print(Tampon)
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            if Tampon[boxx][boxy] == -1:
                filled[boxx][boxy] = False
            if Tampon[boxx][boxy] == 2:
                filled[boxx][boxy] = True

    drawBoard(0, filled, BOXCOLOR)

##==============================================================================


if __name__ == '__main__':
    main()
