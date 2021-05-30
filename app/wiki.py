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

	def extracts_text_with_title(self):
		if self.title != '':
			self.params = { "action": "query", 
				"prop": "extracts", 
				"exsentences": 2, 
				"exlimit": 1, 
				"titles": str(self.title), 
				"explaintext": 1, 
				"format": "json"
			}
			self.response = self.request.get(url=self.url, params=self.params)
		
			if self.response.status_code == 200:
				self.data = self.response.json()

				"""get the pageId, for extract the text content"""
				try:
					for key, value in self.data['query']['pages'].items(): 
						self.pageId = key
						return self.data['query']['pages'][self.pageId]['extract']
				except Exception as e:
					return ''
			else:
				return ''
		else:
			return ''

	def get_title_with_geosearch(self):
		#"https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=37.7891838%7C-122.4033522&gsradius=10000&gslimit=100&format=json".format(self.location['lat'], self.location['lng'])
		
		if self.location != '':
			url = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord={0}%7C{1}&gsradius=10000&gslimit=100&format=json".format(self.location['lat'], self.location['lng'])
			'''
			payload={
				'action': 'query',
				'list': 'geosearch',
				'gsradius': 10000,
				'gslimit':100,
				'format': 'json',
				'gscoord': '37.7891838%7C-122.4033522'
			}
			'''

			response = self.request.get(url=url)

			if response.status_code == 200:
				try:
					return response.json()['query']['geosearch'][0]['title']
				except Exception as e:
					return ''
			else:
				return ''
		else:
			return ''

	def main(self):
		response = self.extracts_text_with_title()
		if response != '':
			return response
		else:
			response = self.get_title_with_geosearch()
			if response != '':
				self.title = response
				response = self.extracts_text_with_title()
				return response
			else:
				return ''
