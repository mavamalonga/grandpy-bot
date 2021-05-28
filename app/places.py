import requests

class Places:
    """docstring for Find_place"""
    def __init__(self, key, title):
        self.key = key
        self.title = title
        self.url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        
    def get_geolocation(self):
        self.params = {
            'key': self.key, 
            'input': self.title,
            'inputtype':'textquery',
            'fields': 'geometry'
        }
    
        data = requests.get(self.url, self.params)
        if data.status_code == 200:
            response = data.json()
            try:
                return response['candidates'][0]['geometry']['location']
            except Exception as e:
                return 'Not Found.'
        else:
            return 'Not Found.'
