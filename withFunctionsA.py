import requests
from bs4 import BeautifulSoup
from sys import argv



def termIn(term):
	terms = term
	url = "http://www.investopedia.com/search/default.aspx?q="
	url = url + terms.replace(" ", "%20")
	if(url[-3:] != "%20"):
		url = url + "%20" + "definition"
	else:
		url = url + "definition"

	return searchUrl(url)
	
def searchUrl(url):
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
			#print temp 


	z = requests.get(temp)

	sope = BeautifulSoup(z.content)
	p_data = sope.find_all("p")

	j = 0
	temp = ""
	for i in p_data:
		if(j < 2):
			temp = temp + i.text 
			j += 1
		else:
			break
	temp += '\n'
	return temp

script, fin, fout = argv

indata = open(fin)
out_file = open(fout, 'w')

for line in indata:
	out_file.write(termIn(line))


out_file.close()




