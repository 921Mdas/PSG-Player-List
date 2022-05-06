import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://partir.ouest-france.fr/congo/budget"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"lxml")

# test connection
results = []
prix = ''
tables = soup.find('div', id="cat-1").find_all('td')

for item in tables:
        prices = {}
        desc = item.find('span', {'class','only-desktop'})
        if item.text.find('$') > -1 :
                     prix = item.text
        if desc == None:
            continue
        else:
            prices['menu']= desc.text
            prices['prix']=  prix.replace('$','')
            results.append(prices)
        


final = pd.DataFrame(results) 
expensive = final['prix'].tail(4)
print(expensive)


# result = soup.extract()

# tst = soup.head
# tst = soup.title
# tst = soup.body.find_all('a')
# tst = soup.table.contents

# tst = soup.table.children >>> iterator can loop through

# tables = soup.find(id= 'cat-1')
# zo = tables.table.find_all('tr', {'class','odd'})

# prices = []
# for i in zo:
#    prices.append({i.td.text: i.td.find_next('td').text})
# print(prices)


# for link in tst:
#     if link['href'].startswith('http'):
#         continue
#     print(link['href'])

# print(tst)


# tst = soup.find('table', {'class','data-table'}).text
# co = tst.rsplit("$")
# print(co)

# for t in co:
#     if t.find('$') > -1:
#         print(t)

# for td in tst:
#    item = td.get('td', {'class','head-prix'})
#    print(item)


