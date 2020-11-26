key = input("What keyword should I use to search: ")
from googlesearch import search 


print("\nSearching for Movie\n")
try:
    l=[]
    for j in search(key, tld="co.in", num=50, stop=50, pause=2): 
        if 'https://www.imdb.com/title' in j:
            movieurl = j
            break
            
except:
    print('Error Occured')
    
import requests
url = requests.get(j).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(url,'lxml')

listed = soup.find('div',{'class':"redesign"})
a = listed.find('div',{'class':'pagecontent'})
b = a.find('div',{'class':'flatland'})
c = b.find('div',{'class':'main'})
d = c.find('div',{'class':'heroic-overview'})
e = d.find('div',{'class':'vital'})
f = e.find('div',{'class':'title_bar_wrapper'})

g = f.find('div',{'class':'ratingValue'})
rating = g.find('span',{'itemprop':'ratingValue'}).text

h = f.find('div',{'class':'title_wrapper'})
name = h.find('h1').text

i = d.find('div',{'class':"plot_summary"})
story = i.find('div',{'class':'summary_text'}).text
story = story.replace('  ','')

print(f"Name: {name}, Rating: {rating}\nStory: {story}")

