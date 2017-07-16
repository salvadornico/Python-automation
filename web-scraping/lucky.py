#! python3
# Launches the first three Google search results in separate tabs

import requests, sys, webbrowser, bs4

print('Googling..')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
# pick out links inside <h3>'s with class="r"
linkElems = soup.select('.r a')

# open tabs for the top five results or all results, whichever is lower
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))