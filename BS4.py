import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://www.bbc.com').read()
soup = bs.BeautifulSoup(sauce,'lxml')
print(soup.title)
for paragraph in soup.find_all('a'):
	print(paragraph.text)