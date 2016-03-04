#!/usr/bin/python3
# -*-coding:utf-8 -*

""" ce programme permet de stocker les 5 meilleurs scores et de les afficher"""


import pickle

def saveNewScore(score, playerName):
	try:
		with open("top5","rb") as f:
			pick = pickle.Unpickler(f)
			top5 = pick.load()
	except:
		top5 = [(0,''),(0,''),(0,''),(0,''),(0,'')]
	top5.append((score,playerName))	
	top5.sort(reverse=True)
	top5 = top5[:5]

	with open("top5","wb") as f:
		pick = pickle.Pickler(f)
		pick.dump(top5)

def printScore():
	with open("top5","rb") as f:
		pick = pickle.Unpickler(f)
		top5 = pick.load()
	print("\n---- SCORE TOP 5 -----")
	print(top5)
	print("\n")