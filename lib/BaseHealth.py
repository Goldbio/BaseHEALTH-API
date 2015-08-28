import requests
from bs4 import BeautifulSoup

class API:

	def __init__( self, key ):
		self.key = key
		self.baseURL = 'https://api.basehealth.com/Genophen/api/v1/' 

	def getCuratedContent( self, disease ):
		r = requests.get( self.baseURL + 'diseases/' + disease , headers= { 'user_key': self.key } )
		return r.json()

	def getAllDiseases(self):
		r = requests.get( 'https://developer.basehealth.com/ndocs/CuratedContent' )
		soup = BeautifulSoup( r.text , 'html.parser')

		return r.text
		#return soup.find_all('div', class_='heading' )


		
		



