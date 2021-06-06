#!/usr/bin/python3

"""
    search.py

    MediaWiki API Demos
    Demo of `Search` module: Search for a text or title

    MIT License
"""
import requests

class MediaWiki:
	"""docstring for ClassName"""
	def __init__(self, title, location=None):

		self.url = "https://fr.wikipedia.org/w/api.php"
		self.request = requests.Session()
		self.title = title
		self.location = location

	def filter_word(self, word):

		word = word.replace('(', '')
		word = word.replace(')', '')
		word = word.replace('-', ' ')

		new_split = word.split()

		if len(new_split) > 1:
			return new_split
		else:
			return word

	def compare_number_common_word(self, t_word, word_form_content):
		try:
			if type(t_word) == 'str':
				for f_word in word_form_content:
					if t_word.lower() == f_word.lower():
						nb_common_word += 1
		except Exception as e:
			for tt_word in t_word:
				for f_word in word_form_content:
					if t_word.lower() == f_word.lower():
						nb_common_word += 1
		finally:
			return nb_common_word


	def select_title_with_more_common_word(self):

		word_form_content = self.title.split() # on recupere les mots cles de la recherche
		PAGES = self.prefixsearch()

		max_common_word = 0
		nb_common_word = 0
		pageid = 0
		for page in PAGES:              # On recupere chaque resulatat de la recherche mediwii
			title_list_word = page['title'].split()     # On separer chaque mot du titre

			for t_word in title_list_word:
				t_word = self.filter_word(t_word)
				nb_common_word = self.compare_number_common_word(t_word, word_form_content)

			if nb_common_word > max_common_word:
				max_common_word = nb_common_word
				pageid = page['pageid']
			nb_common_word = 0

		return pageid
		

	def extracts_text(self, pageId):

		self.params = { 
			"action": "query",
			"prop": "extracts",
			"exsentences": 10,
			"exlimit":1,
			"pageids": pageId,
			"explaintext":1,
			"format": "json"
		}
		
		self.response = self.request.get(url=self.url, params=self.params)
		
		if self.response.status_code == 200:
			try:
				self.data = self.response.json()
				for key, value in self.data['query']['pages'].items():
					return value['extract']
			except:
				return 'Failed request'
		else:
			return 'Failed request'



	def prefixsearch(self):
		"""Perform a prefix search for page titles"""
		S = requests.Session()

		URL = "https://fr.wikipedia.org/w/api.php"

		PARAMS = {
    		"action": "query",
    		"format": "json",
    		"list": "prefixsearch",
    		"pssearch": str(self.title)
		}

		R = S.get(url=URL, params=PARAMS)

		if R.status_code == 200:
			try:
				DATA = R.json()
				PAGES = DATA['query']['prefixsearch']
				return PAGES
			except:
				return 'Failed request'
		else:
			return 'Failed request'

	def main(self):
		pageid = self.prefixsearch()
		text = self.extracts_text(pageId)
		return text



m = MediaWiki('avenue charles de gaule')
print(m.select_title_with_more_common_word())