{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fnil\fcharset0 Cambria;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww16640\viewh16020\viewkind0
\deftab708
\pard\pardeftab708\ri-386\partightenfactor0

\f0\fs24 \cf0 import turtle\
turtle.tracer(0,0)            # acc\'e9l\'e9ration du trac\'e9\
turtle.screensize(2000,2000)  # taille fen\'eatre graphique\
turtle.pu()\
turtle.goto(-500,0)\
turtle.pd()\
\
def dessiner(courbe, longueur, angle):    \
    """ r\'e9alise une repr\'e9sentation graphique d'une courbe donn\'e9e par des chaines de caract\'e8res """\
    for caractere in courbe:\
        if caractere == '+': turtle.left(angle)\
        elif caractere == '-': turtle.right(angle)\
        elif caractere in ['F', 'G']: turtle.forward(longueur)\
\
def reglesierpinski(chaine):\
    nouvelleChaine = ''    # on cr\'e9e une nouvelle chaine de caract\'e8res VIDE\
    for lettre in chaine:  # on \'e9pelle la chaine de caract\'e8res donn\'e9e en param\'e8tres\
        if lettre == 'F':  # si dans l'ancienne chaine, il y a un 'F'\
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'  # alors, on \'e9crit F-G+F+G-F dans la nouvelle chaine\
        elif lettre == 'G':\
            nouvelleChaine = nouvelleChaine + 'GG'  # alors, on \'e9crit GG dans la nouvelle chaine\
        else :\
            nouvelleChaine = nouvelleChaine + lettre  # sinon, on reporte la lettre telle quelle\
    return nouvelleChaine\
\
def courbesierpinski(motifInitial, niter):\
    """ \
        appelle niter fois regleKoch pour cr\'e9er la courbe de Koch\
    """\
    courbe = motifInitial # on part du motif initial donn\'e9 par l'utilisateur en param\'e8tres\
    for i in range(niter):\
        nouveauMotif = reglesierpinski(courbe)  # on trouve le nouveau Motif \'e0 partir du motif de d\'e9part\
        courbe = nouveauMotif # on dit que le nouveau Motif est maintenant le motif de d\'e9part\
    return courbe\
\
longueur = 10\
angle = -120\
niter = 6\
dessiner(courbesierpinski('F-G-G', niter), longueur, angle)\
\
turtle.update()      # acc\'e9l\'e9ration du trac\'e9\
turtle.exitonclick() # permet la fermeture de la fen\'eatre graphique\
}