import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

f= open("$HOME/BERNIE_NAMES_AND_SITES.txt","a+")

names = []

for i in range(40):

	urlpage = 'https://www.stories.berniesanders.com/page/' + str(i+1)
	
	driver = webdriver.Firefox()
	driver.get(urlpage)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
	time.sleep(5)

	results = driver.page_source

	soup = BeautifulSoup(results,features="html5lib")
	
	find_cards = 'div[class*="tile-item snack-card-container"]'
	find_name = 'div[class*="snack-attribution-name"]'
	
	for card in soup.select(find_cards):
		for name in card.select(find_name):
			name = name.get_text()
		for url in card.find_all('a'):
			text = url.attrs['style']
			text = text.replace('background-image: url(https://assets.stories.berniesanders.com/video/anonymous/','https://www.stories.berniesanders.com/videos/')
			text = text.replace('/720p-00001.png)','')
		
		f.write(name + ',' + text + '\n')

		
	driver.quit()


f.close()
