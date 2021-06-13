import random

class Brain:
	dictionary = {
		'presentation': ['Bonjour moi c\'est grandpy'],
		'catch': ['Salut moi c\'est grandpy, je suis content de vous ', 
				'Ahahah c\'est trop cool, j\'ai de la visite !',
				 'Afin quelqu\'un avec qui echanger.'],
		'response': ['Très bien'],
		'not_understand': ['Je n\'ai pas compris ta réponse', 'Peut-tu repeter ta question stp ?']
		}

	def __init__(self):
		pass

	def say(self):
		return random.choice(self.dictionary['presentation'])


