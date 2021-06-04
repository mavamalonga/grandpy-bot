

class Parse:
	"""docstring for ClassName"""

	form = ['Que', 'Quand', 'Pourquoi','Quel', 'Quelle', 'Lequel', 'Comment','je', 'tu', 'il', 'elle', 'on', 
	'nous', 'vous', 'ils', 'elles','le', 'les', 'la','mais', 'ou', 'et', 'donc', 'or', 
	'ni', 'car','?', 'est', 'plus', 'des', 'sur', 'mon']

	key = ['pourquoi', 'Avenue', 'rue', 'bar', 'restaurant']


	def __init__(self, question):
		self.question = question

	def removes_unnecessary_words(self):
		for word in self.form:
			if self.word == word:
				return False
			
		return True

		#select start by 'x' and where len(word) = size


	def split_question (self):
		self.key_words = []
		self.question = self.question.split()
		for self.word in self.question:
			if len(self.word) >= 3:
				re = self.removes_unnecessary_words()
				if re == True:
					self.key_words.append(self.word)

		if len(self.key_words) >= 2:
			self.question = self.key_words
			return self.question
		else:
			return self.key_words


	def main(self):
		res = self.split_question()





p = Parse('Avenue des charles de Gaule')
print(p.split_question())