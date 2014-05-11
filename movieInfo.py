#################################
#                               #
#     Author: Anoop S           #
#                               #
#################################


from bs4 import BeautifulSoup
import requests

prompt = raw_input("Enter movie name\n")
result = requests.get("http://www.google.com/search?q="+prompt.replace(' ','+')+'+imdb')
page = result.text.encode('ascii','ignore')
result.close()

soup = BeautifulSoup(page)
element = soup.select("div cite")

element = map(lambda x: str(x.text),element)
imdbLinks = filter(lambda x: len(x.split('/'))==4 and x.split('.')[1]=='imdb',element)

print str(len(imdbLinks))+" result(s) fetched"

for each in imdbLinks:
    result = requests.get("http://"+each)
    page = result.text.encode('ascii','ignore')
    result.close()
    soup = BeautifulSoup(page)
    name = soup.find("span",{'itemprop':'name'})
    print "Movie is :"+name.text
    rating = soup.find("div",{'class':'titlePageSprite star-box-giga-star'})
    if rating:
        print "Rating is :"+rating.text
    else:
        print "Rating not present"
    genre = soup.findAll("span",{'class':'itemprop','itemprop':'genre'})
    genre = map(lambda x:x.text,genre)
    print 'Genre is :'+'|'.join(genre)
    print
    print
    
