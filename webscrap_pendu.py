#!/usr/bin/python3
# -*-coding:utf-8 -*

""" programme qui va chercher les mots du dictionnaires sur le site internet 
http://www.encyclopedie-incomplete.com/?Les-600-Mots-Francais-Les-Plus#outil_sommaire_3
Ils sont tous places dans: list_dico, de type list().
Reference: http://docs.python-guide.org/en/latest/scenarios/scrape/"""

from lxml import html
import requests

page = requests.get("http://www.encyclopedie-incomplete.com/?Les-600-Mots-Francais-Les-Plus#outil_sommaire_3")
#page.text contient toute la source html de la page sous format str()
#le type de page est : <class 'requests.models.Response'>
tree = html.fromstring(page.content)
#p.content c'est pareil que p.text mais en format binaire


#Et voici la partie qui dechire avec la super methode .xpath:
#Apres une analyse rapide du code source de la page,
#les mots recherches sont compris dans des balises:
#<tr class=XXX><td><strong> UN MOT </strong>...
#,où la class XXX est soit 'row_even' soit 'row_odd'
mot_1 = tree.xpath('//tr[@class="row_even"]/td/strong/text()')
#..en plus SublimText propose lui meme le nom de la class !
#Bon par contre l'argument du xpath est encore a etudier. Jai pas tout compris
mot_2 = tree.xpath('//tr[@class="row_odd"]/td/strong/text()')
list_dico=mot_1+mot_2