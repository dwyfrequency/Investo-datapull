import requests
from bs4 import BeautifulSoup

url = "http://www.investopedia.com/terms/m/mutualfund.asp"

r = requests.get(url)

soup = BeautifulSoup(r.content)
p_data = soup.find_all("p")


j = 0
for i in p_data:
	if(j < 2):
		print i.text 
		print '\n'
		j += 1
	else:
		break
	