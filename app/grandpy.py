import random

class Vocabulary:

	catch_phrase = ['Salut moi c\'est grandpy, comment allez vous ?', 
	'Ahahah c\'est trop cool, j\'ai de la visite !', 'Afin quelqu\'un avec qui echanger.']

	understand = ['Désolez pourriez vous reformuler la phrase s\'il vout plait, j\'ai u peu du mal à compndre.']

	reponse = ['Je parle francais, et actuellement je suis entrein d\'apprendre l\'anglais']

	def __init__(self):
		pass

	def say(self):
		return random.choice(self.catch_phrase)

