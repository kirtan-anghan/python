import requests,sys,webbrowser,bs4

res = requests.get('http://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")
linkelement = soup.select('.r a')
linktoopen = min(5,len(linkelement))
for i in range(linktoopen):
    webbrowser.open("https://google.com"+linkelement[i].get('href'))