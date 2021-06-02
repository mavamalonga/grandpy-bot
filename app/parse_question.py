

class Parse:
	"""docstring for ClassName"""
	def __init__(self, question):
		self.question = question
		self.words = []

	def parse_question_formula(self):
		self.formula = ['Est-ce que', 'Parlez-vous', 'Ne partez-vous pas', 'Vont-ils', 'Où est-ce que', 'Pourquoi est-ce que',
		'Comment est-ce que', ]

	def parse_first_name (self):
		self.personal_first_name = ['je', 'tu', 'il', 'on', 'elle', 'nous', 'vous', 'ils', 'elles']
		self.words = self.question.split()
		for count in range(len(self.words)):
			self.question = self.question.replace(self.personal_first_name[count], "")
		return self.question


p = Parse('Je suis content')
print(p.split_words())