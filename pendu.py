#!/usr/bin/python3
# -*-coding:utf-8 -*

""" Jeu pendu.
Utilisation du webscrapping: module requests; module lxml, methode xpath
I/O file: module pickle
On va chercher la liste des mots francais qui pourraient etre le mot secret a trouver.
"""

#Le programme webscrap_pendu.py ,renvoie la liste : list_dico,
#qui contient 600mots francais
import webscrap_pendu as ww
#le programme savetop5_pendu contient deux fonctions pour sauvegarder et afficher le top5 des scores
import savetop5_pendu
import random

score=0 #le score cest le nb de fois a la suite que le joueur trouve le mot mystere

while (input("Voulez vous jouer (y) : ").lower() == "y"):
	#initialisation du jeu:
	nb_chance=10
	mot_mystere = ww.list_dico[round(random.uniform(0,600))] #mot aleatoire
	mot_masque = str()
	for i in mot_mystere:
		mot_masque += "_" #le mot masque est represente par des underscores

	#Debut du jeu :
	while(mot_mystere!=mot_masque and nb_chance>0):
		#affichage des donnees aux joueurs et demande d'une lettre:
		print("\nIl vous reste : {} chances".format(nb_chance))
		print(mot_masque)
		x = input("Choisissez une lettre : ").lower()

		#Check de la lettre dans le mot secret:
		if x not in mot_mystere:
			nb_chance-=1
		#on remplit le mot masque par la(les) lettre(s) dans le(s) bon(s) emplacement(s):
		else:
			i=0
			while (i<len(mot_mystere)):
				if (mot_mystere[i] == x):
					mot_masque=mot_masque[:i] + x + mot_masque[i+1:]
				i+=1

	#Le jeu est fini. Soit le joueur a gagne, soit perdu...
	if(mot_mystere==mot_masque):
		print("\nVous avez gagne !")
		#on incremente le score
		score+=1
		print("Score = ", score)
	elif(nb_chance<=0):
		print("\nVous avez perdu...")
		#on actualise et affiche le top5 des scores
		savetop5_pendu.saveNewScore(score,input("Votre nom :"))
		savetop5_pendu.printScore()
		#le score retombe a zero
		score=0
	print(" Le mot mystere etait :",mot_mystere)
