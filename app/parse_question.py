

class Parse:
	"""docstring for ClassName"""

	insignificant_words = { '2_character': ['a', 'à', 'je', 'tu', 'il', 'on', 'le', 'la', 'un', 
		'me', 'ne', 'et', 'de', 'en', 'au', 'ou', 'si', 'où', 'ma'],
		'3_character': ['est', 'les', 'pas', 'les', 'mon', 'ses', 'des', 'une', 'qui'],
		'8_character': 'pourquoi', 
		'7_character': 'comment',
		'5_character': 'quand' 
		}

	def __init__(self, question):
		self.question = question.split()


	def delete_words(self):
		only_key_words = []
		for word in self.question:
			if len(word) == 2:
				for re in self.insignificant_words['2_character']:
					if re.lower() == word.lower():
						res = True
				if res != True:
					only_key_words.append(word)
			elif len(word) == 3:
				for re in self.insignificant_words['3_character']:
					if re.lower() == word.lower():
						res = True
				if res != True:
					only_key_words.append(word)
			elif len(word) == 5:
				if word.lower() != self.insignificant_words['5_character'].lower():
					only_key_words.append(word)
			elif len(word) == 7:
				if word.lower() != self.insignificant_words['7_character'].lower():
					only_key_words.append(word)
			elif len(word) == 8:
				if word.lower() != self.insignificant_words['8_character'].lower():
					only_key_words.append(word)
			else:
				only_key_words.append(word)

			res = False
		return only_key_words

	def concat(self, only_key_words):
		for word in only_key_words:
			question = word + ' '
		return only_key_words

	def main(self):
		if len(self.question) > 3:
			question = self.delete_words()
			question = self.concat(question)
		else:
			question = self.concat(self.question)
		return question


P = Parse('pourquoi les puces piquent')
print(P.main())