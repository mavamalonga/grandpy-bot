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

	def select_title(self):
		pass

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
print(m.prefixsearch())