import random
import datetime


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

	def main(self):
		x = datetime.datetime.now()
		time = x.strftime("%H") + ":" + x.strftime("%M")
		return {'phrase': random.choice(self.dictionary['presentation']),
				'time': time
				}


