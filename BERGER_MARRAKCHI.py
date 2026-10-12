"""
The Legend of the Dot Escape - Python Escape Game (2022)

Authors: Emilion Berger and Johan Marrakchi

Collaborative programming project developed for the online course
"Apprendre a coder avec Python" on FUN-MOOC.

Last update: 16/11/2022 21:00

Description:
A Python escape game featuring a castle maze, locked doors with
questions and answers, collectible objects, and an inventory system.
"""
import turtle
import time
from CONFIGS import *


# Fonctions dans le but de raccourcir le code ou de le clarifier
def depl(tur, pos):
    """Fonction dans le but de raccourcir le code
    Deplace une tortue en la levant et rabaissant
    Prend en parametre la tortue a deplacer et la position d'arrivée"""
    tur.up()
    tur.goto(pos)
    tur.down()


def ann_write(text):
    """Fonction dans le but de raccourcir le code
    Deplace la tortue "ann" dans la zone d affichage des annonces, efface les dessins de "ann" et ecrit le texte
    en parametre"""
    depl(ann, POINT_AFFICHAGE_ANNONCES)
    ann.clear()                                              # efface tout le texte precedement ecrit par ann
    ann.write(text)                                          # ecrit le texte donné comme parametre dans la zone annonce


def jump(taille_x):
    """"Fonction dans le but de raccourcir le code
    Efface le personnage de la case, redefinis posi decalée d'un cran en fonction du deplacement (donné en parametre),
    et pose le personnage dans la case d'apres (en fonction de posi)"""
    global posi
    print_case()                                              # enlever personnage de case
    posi = (posi[0] + taille_x[0], posi[1] + taille_x[1])     # avance posi d'une case (dans le deplacement effectué)
    case_personnage(posi)                                     # reposer personnage case suivante


def dic(fichier, dico):
    """ Fonction dans le but de raccourcir le code
    Prend un fichier et un dictionnaire en parametre et rajoute toutes les lignes du fichier comme elements du
    dictionnaire"""
    with open(fichier, "r", encoding="utf-8") as fich:        # ouvre le fichier donné en parametre
        z = fich.readlines()                                  # lis chaque ligne et les met en element d une liste
        for i in z:                                           # prend chaque ligne une par une
            a, b = eval(i)                                    # assigne i[0] a "a" et i[1] a "b"
            dico[a] = b                                       # rajoute b dans le dictionnaire avec "a" comme clée


def donne_nbre_case(fichier):
    """Fonction dont le but est de raccourcir le corps texte et le rendre plus lisible"""
    with open(fichier, "r", encoding="utf-8") as plan:        # ouvre le fichier donné en parametre
        u = plan.readlines()[0]                               # lis la premiere ligne du fichier
        u = u.strip()                                         # supprime le "\n" de la ligne
        u = u.split()                                         # supprime les espaces de u
        cases = len(u)                                        # calcule le nombre de case pour la ligne 1
        return cases


# Partie 1 : Le Plan
def lire_matrice(plan):
    """Fonction qui prend en parametre une matrice en fichier texte et la transforme en liste pour enfin créer le plan
    du chateau via cette matrice, les numéros symbolisants chacun un type de case"""
    depl(turtle, pos_coin)
    with open(plan, "r", encoding="utf-8") as plan:
        docu = {0: COULEUR_CASES, 1: COULEUR_MUR, 2: COULEUR_OBJECTIF, 3: COULEUR_PORTE, 4: COULEUR_OBJET}
        for i in plan.readlines():                           # lis chaque ligne et les met en element d une liste
            i = i.strip()                                    # supprime le "\n" de la ligne
            i = i.split()                                    # supprime les espaces de u
            for a in i:
                print_case(col2=docu[int(a)])                # dessine la case avec la couleur dependant de son numero
                turtle.up()
                turtle.forward(taille[0])                    # avance jusqu'a la position de la case suivante
                turtle.down()
            turtle.up()
            turtle.backward(taille[0]*len(list(i)))          # apres avoir fait toute la ligne, recule jusqu au depart
            turtle.right(90)                                 #
            turtle.forward(taille[0])                        # et descend d une case pour faire la ligne d'apres
            turtle.left(90)
            turtle.down()


def case_personnage(pos):
    """Fonction qui dessine le personnage (sous forme de rond) au milieu de la case de la position donné en parametre"""
    pos2 = (pos[0] - taille[0]/2, pos[1] + taille[1]/2)     # definis pos2, la position du centre de la case
    depl(turtle, pos)
    print_case()                                            # dessine la case (avec COULEUR_VUE en fond)
    depl(turtle, pos2)
    turtle.dot(int(taille[0]*RATIO_PERSONNAGE), COULEUR_PERSONNAGE)
    # dessine le personnage avec comme centre pos2, avec un certain ratio et une certaine couleur
    depl(turtle, pos)


# Partie 2 : Les Déplacements
def print_case(col1=COULEUR_EXTERIEUR, col2=COULEUR_VUE):
    """Fonction qui redessine la case ou est la tortue actuellement en la coloriant avec les couleurs données en
    parametre; Dans le principe, sert a faire disparaitre les objets et murs et a avoir un suivi des cases sur
    lesquelles on est passé"""
    turtle.color(col1, col2)                               # choisis la couleur extérieur et interieur de la tortue
    turtle.begin_fill()                                    # commence a remplir avec la couleur interieur
    for i in range(4):
        turtle.left(90)
        turtle.forward(taille[0])
    turtle.end_fill()                                      # finis de remplir


def mouv(taille_x):
    """Fonction coordonnant les autres fonctions de deplacement pour effectuer ou mouvement ou non en fonction de la
    case de destination, le parametre donne la direction du mouvement en question"""
    global fichier_plan, posi, taille, Affichage_objet, cond
    # definis quelques (beaucoup ^^') de variables comme globales
    with open(fichier_plan, "r", encoding="utf-8") as plan:  # ouvre le fichier donné comme parametre
        v = plan.readlines()                                 # lis les lignes du fichier et les mets comme elem de liste
        v = v[(pos_coin[1]-(taille_x[1]+posi[1]))//taille[1]].strip()
        # prend la ligne correspondant a l'ordonnée de la case cible du deplacement et enleve le "\n"
        v = v.split()                                        # enleve les espaces de la ligne
        num = int(v[(posi[0]+taille_x[0]-pos_coin[0])//taille[0]])
        # calcule num de la case cible du mouvement
        if num == 0 or num == 4:                             # si case franchissable
            jump(taille_x)
            # deplace le personnage sur la case voulue et remplace celle-ci par une case vue
            if num == 4:                                     # si case = objet
                objet()
                # ajoute l' objet a l inventaire, ecris l action effectuée dans la zone annonce,...
        if num == 3:                                         # si case = porte
            portes(taille_x)                                 # lance la fonction portes qui pose la question prévue,...
        if num == 2:                                         # si case = case finale
            victory(posi, taille_x)                          # lance fonction victory qui finit le jeu


def deplacement_gauche():
    """Fonction qui enclenche un mouvement du personnage vers la gauche en appelant la fonction mouv"""
    turtle.onkeypress(None, "Left")                          # desactive la touche
    taille_gauche = (-taille[0], 0)                          # definis le pas de case a faire
    mouv(taille_gauche)                                      # lance la fonction mouv pour faire le deplacement
    turtle.onkeypress(deplacement_gauche, "Left")            # reactive la touche


def deplacement_droite():
    """Fonction qui enclenche un mouvement du personnage vers la droite en appelant la fonction mouv"""
    turtle.onkeypress(None, "Right")                         # desactive la touche
    taille_droite = (taille[0], 0)                           # definis le pas de case a faire
    mouv(taille_droite)                                      # lance la fonction mouv pour faire le deplacement
    turtle.onkeypress(deplacement_droite, "Right")           # reactive la touche


def deplacement_haut():
    """Fonction qui enclenche un mouvement du personnage vers le haut en appelant la fonction mouv"""
    turtle.onkeypress(None, "Up")                            # desactive la touche
    taille_haut = (0, taille[1])                             # definis le pas de case a faire
    mouv(taille_haut)                                        # lance la fonction mouv pour faire le deplacement
    turtle.onkeypress(deplacement_haut, "Up")                # reactive la touche


def deplacement_bas():
    """Fonction qui enclenche un mouvement du personnage vers le bas en appelant la fonction mouv"""
    turtle.onkeypress(None, "Down")                          # desactive la touche
    taille_bas = (0, -taille[1])                             # definis le pas de case a faire
    mouv(taille_bas)                                         # lance la fonction mouv pour faire le deplacement
    turtle.onkeypress(deplacement_bas, "Down")               # reactive la touche


# Partie 3 : Les Objets
def print_texte(pos):
    """"Fonction qui écris dans la zone d'annonce l'objet trouvé et l ajoute a l'inventaire via le parametre
    qui est la position de l'objet puis supprime l'objet du dictionnaire"""
    turtle.color("black")                                   # change la couleur de turtle
    depl(ann, POINT_AFFICHAGE_ANNONCES)                     # deplace ann dans la zone annonce
    ann.clear()                                             # efface ce que ann a ecrit precedement
    ann.write("Vous avez trouvé un objet : " + d[pos])      # ecrit avec ann ce qui est demandé
    depl(turtle, Affichage_objet)                           # deplace turtle a la zone d affichage objet
    turtle.write(str(pos) + " " + d[pos])                   # ecrit la position et l objet dans la zone affichage objet
    depl(turtle, posi)                                      # remet turtle a posi
    del d[pos]                                              # supprime pos de d pour ne plus le rajouter si on repasse


def objet():
    """Fonction qui calule la position en prenant comme origine la case en haut a gauche et une case comme unité,
    puis appelle la fonction print_texte en fonction de cette position"""
    global Affichage_objet                                 # definie la position affichage objet comme variable globale
    posi_theorique = ((- posi[1] + pos_coin[1]) // taille[1], (posi[0] - pos_coin[0]) // taille[0])
    # definis la posi théorique actuelle (posi en prenant (0,0) en haut a droite du laby et (1, 0) la posi de depart
    if posi_theorique in d:                                # si cette position et dans d
        Affichage_objet = (Affichage_objet[0], Affichage_objet[1] - 10)
        # descend d'un cran l'ecriture de l objet dans l'inventaire
        print_texte(posi_theorique)                        # ecris l objet dans la zone inventaire et dans l annonce


# Partie 4: Les Portes
def portes(taille_var):
    """Fonction appellée lors d'un deplacement vers une porte qui detecte quelle porte c'est grace au dico_portes et au
    parametre la destination potentielle et pose la question correspondante a celle-ci, si la reponse est correcte,
    la fonction va enlever la porte du dictionnaire et ecrire "La porte s'ouvre" dans la zone annonce, sinon,
    ecrire "La porte reste fermée"""
    posi_theorique = ((- (posi[1] + taille_var[1]) + pos_coin[1]) // taille[1],
                      (posi[0] + taille_var[0] - pos_coin[0]) // taille[0])
    # definis la posi théorique (prochaine) (posi en prenant (0,0) en haut a droite du laby et (1, 0) la posi de depart
    if posi_theorique in doc:                             # si on est pas encore passé dessus
        question = turtle.textinput("Question", doc[posi_theorique][0])
        # pose la question et stock la reponse
        if question == doc[posi_theorique][1]:            # si la reponse est bonne
            ann_write("La porte s'ouvre")
            del doc[posi_theorique]                       # supprime l element du doc pour qu on puisse passer dessus
        else:                                             # sans probleme par apres
            ann_write("La porte reste fermée")
    if posi_theorique not in doc:                         # permet d avancer si l element n est pas dans le doc
        jump(taille_var)
    turtle.listen()                                       # permet de reecouter les touches claviers


def victory(pos, taille_x):
    """Fonction appelée si le personnage arrive sur la case finale, ce qui fait apparaitre le mot "VICTOIRE" en grand
    et ferme le jeu apres un court delais"""
    if d == {}:                                              # si d est vide (si on a recup tous les objets)
        print_case()                                         # dessine la case (avec COULEUR_VUE en fond)
        pos = (pos[0] + taille_x[0], pos[1] + taille_x[1])   # redefinis pos deplacé dans le mouvement voulu
        case_personnage(pos)                                 # place le personnage sur la case finale
        turtle.color("red")                                  # chance de couleur turtle
        depl(turtle, (-300, -32))                            # deplace turtle a la position donnée
        turtle.write("VICTOIRE", font=("Arial", 64, "normal"))
        # ecris en gros et rouge "VICTOIRE"
        time.sleep(1)                                        # laisse s'écouler 1 seconde (en realité + mais bon)
        turtle.bye()                                         # ferme la fenetre
    else:
        depl(ann, POINT_AFFICHAGE_ANNONCES)                  # deplace ann dans la zone d annonce
        ann.clear()                                          # efface tout ce que ann a fait
        ann.write("Vous ne possédez pas tous les indices")   # ecris le texte voulu a la place


# debut du corps texte
turtle.tracer(0, 0)                                          # rend les dessins instantanés
turtle.title("The Legend Of The Dot Escape")                 # donne le titre donné a la fenetre

# parametres de base
nbre_case = donne_nbre_case(fichier_plan)                    # donne le nombre de case via la fonction donne_nbre_case
taille_plan = (ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0], ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1])
# definis la taille du plan via les parametres donnés de la zone du plan
taille = (min(taille_plan[0]//nbre_case, taille_plan[1]//nbre_case),
          min(taille_plan[0]//nbre_case, taille_plan[1]//nbre_case))
# definis la taille des cases en fonction de la taille du plan, et symetrise x et y pour avoir des carrés
pos_coin = (min(ZONE_PLAN_MINI[0], ZONE_PLAN_MINI[0]) + taille[0], max(ZONE_PLAN_MAXI[1], ZONE_PLAN_MINI[1])-taille[1])
# donne la position du coin en haut a gauche (decale de "taille" pour avoir le bas a droite de la case du coin)
posi = (pos_coin[0] + taille[0], pos_coin[1])                # definis la position actuelle (de depart dans ce cas)
                                                             # comme la position de coin decalé d une case a droite
Affichage_objet = POINT_AFFICHAGE_INVENTAIRE                 # fait une copie de POINT_AFFICHAGE_INVENTAIRE
                                                             # pour qu'on puisse le modifier simplement
d = {}                                                       # cree un dictionnaire vide qui recevra les objets
dic(fichier_objets, d)                                       # remplis d grace a la fonction dic()
doc = {}                                                     # cree un dictionnaire vide qui recevra les questions
dic(fichier_questions, doc)                                  # remplis d grace a la fonction dic()

ann = turtle.Turtle()                                        # demarre une autre tortue pour ecrire des annonces
                                                             # et les suppr facilement
# conditions de base
lire_matrice(fichier_plan)                                   # crée le plan
case_personnage(posi)                                        # dessine le personnage a sa position initiale
depl(turtle, POINT_AFFICHAGE_INVENTAIRE)                     # deplace turtle dans la zone d inventaire
turtle.color("black")                                        # change la couleur de turtle en noir
turtle.write("Inventaire : ")                                # ecris le texte donné (le "titre" de la partie inventaire)
depl(turtle, posi)                                           # repose turtle a la position initiale

# gestion deplacement
turtle.listen()  # lire les touches du clavier
turtle.onkeypress(deplacement_gauche, "Left")                # associe une fonction a la touche pressée
turtle.onkeypress(deplacement_droite, "Right")               # associe une fonction a la touche pressée
turtle.onkeypress(deplacement_haut, "Up")                    # associe une fonction a la touche pressée
turtle.onkeypress(deplacement_bas, "Down")                   # associe une fonction a la touche pressée

# fin du code
turtle.mainloop()                                            # garde la fenetre active
