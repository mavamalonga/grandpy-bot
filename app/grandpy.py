import random

class Vocabulary:

	catch_phrase = ['Salut moi c\'est grandpy, comment allez vous ?', 'Ahahah c\'est trop cool, j\'ai de la visite !', 'Afin quelqu\'un avec qui echanger.']

	def __init__(self):
		pass

	def say(self):
		return random.choice(self.catch_phrase)


b = Vocabulary()
print(b.say())