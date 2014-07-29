#################################
#                               #
#     Author: Anoop S           #
#                               #
#################################

from bs4 import BeautifulSoup
import requests

user_input = 'y'
while user_input == 'y':
    
    prompt = raw_input("Enter movie name\n")
    result = requests.get("http://www.google.com/search?q="+prompt.replace(' ','+')+'+imdb')
    page = result.text.encode('ascii','ignore')
    result.close()

    soup = BeautifulSoup(page)
    element = soup.select("div cite")

    element = map(lambda x: str(x.text),element)
    imdbLinks = filter(lambda x: len(x.split('/'))==4 and x.split('.')[1]=='imdb' and x.split('/')[1]=='title' and x.endswith('/'),element)

    print str(len(imdbLinks))+" result(s) fetched\n"


    for each in imdbLinks:
        result = requests.get("http://"+each)
        page = result.text.encode('ascii','ignore') 
        result.close()
        soup = BeautifulSoup(page)
        name = soup.find("span",{'itemprop':'name'})
        year = soup.select('h1[class="header"] span[class="nobr"]')
        print "Movie is :"+name.text+' '+year[0].text
        rating = soup.find("div",{'class':'titlePageSprite star-box-giga-star'})
        if rating:
            print "Rating is :"+rating.text
        else:
            print "Rating not present"
        genre = soup.findAll("span",{'class':'itemprop','itemprop':'genre'})
        genre = map(lambda x:x.text,genre)
        cast = soup.select('table[class="cast_list"] tr td[class="itemprop"] a span')
        print 'Genre is :'+'|'.join(genre)
        print
        if cast:
            print 'Cast includes:'
            cast = map(lambda x:x.text, cast)
            print ','.join(cast)
        print
        print
        
    user_input = raw_input('do you want to search another movie ? y/n: ').lower()
