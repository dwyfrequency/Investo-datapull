import requests
from bs4 import BeautifulSoup

terms = "Liquidity Ratio"
url = "http://www.investopedia.com/search/default.aspx?q="
url = url + terms.replace(" ", "%20")
if(url[-3:] != "%20"):
	url = url + "%20" + "definition"
else:
	url = url + "definition"

r = requests.get(url)

soup = BeautifulSoup(r.content)
links = soup.find_all("a")

lizst = []
for link in links:
	#print link.get("href")
	if(("terms" in link.get("href")) and ("www." in link.get("href"))):
		lizst += link

temp = ""
for i in lizst:
	if(( "www." in i) and ( temp == "")):
		temp = i
		temp = "http://" + temp
		print temp 


z = requests.get(temp)

sope = BeautifulSoup(z.content)
p_data = sope.find_all("p")

j = 0
for i in p_data:
	if(j < 2):
		print i.text 
		print '\n'
		j += 1
	else:
		break
	

#need file of terms to input and read
# file input term
# need to figure out what to do w/ acronyms 
# rneed to replace spaces 
# input[0] to take the first letter of the string 
# endUrl = input[0] + '/' + input + ".asp" 

#url = "http://www.investopedia.com/terms/" + endUrl
#**above will not work b/c url structure is not same
#**across all keyterms