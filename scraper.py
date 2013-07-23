from bs4 import BeautifulSoup
import urllib2
import urllib
import datetime
import sys


def scrape_for_vine(query):
    human_params = "%s vine.co -RT :)" % query
    url = "https://twitter.com/search/realtime?q=%s" % urllib.quote_plus(human_params)
    #return url

    soup = BeautifulSoup( urllib2.urlopen(url).read() )
    arr=[]
    d={}

    for i in soup.find_all('p',{'class':'js-tweet-text'}):
        j = i.get_text().encode('ascii', 'ignore')
        #print j

        for k in j.split():
            if 'vine.co/' in k:
                try:
                    soupe = BeautifulSoup( urllib2.urlopen(k).read() )
                except :
                    #print k
                    e = sys.exc_info()[0]
                    print e
                    break
                try : d['video'] = soupe.find("source").get("src")
                except : d['video'] = 'XXXXX'
                try : d['user_pic'] = soupe.find('div',{'class':'user'}).img.get('src')
                except : d['user_pic'] = 'XXXXX'
                try : d['user'] = soupe.find('div',{'class':'user'}).h2.get_text()
                except : d['user'] = 'XXXXX'
                try : d['tweet'] = soupe.find('div',{'class':'inner'}).get_text()
                except : d['tweet'] = 'XXXXX'
        arr.append(d)
        d={}
        #print 'success'
        
    #for i in arr:
    #    print i['tweet']
    #print arr
    return arr


if __name__ == '__main__':
    print '-------------------> Lets scrape them vines <-------------------'
    print scrape_for_vine("lol")
