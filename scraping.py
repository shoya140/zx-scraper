
# coding: utf-8

# In[1]:



import json
import urllib
import BeautifulSoup
from multiprocessing import Pool


# In[2]:

def scrape(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(html)
    contents = soup.find('div', attrs={'id':'contents'})
    if contents:
        title = soup.find('title').text.encode('utf-8')
        tagBase = soup.find('ul', attrs={'class':'tag_icon'})
        if tagBase:
            tags = [tag.text.encode('utf-8') for tag in tagBase.findAll('li')]
            content = contents.text.encode('utf-8')
            return {'url':url, 'title': title, 'contents':content, 'tags': tags}


# In[3]:

urls = ['http://zexy.net/article/app%09d' %i for i in range(0, 2000)]
pl = Pool()
get_ipython().magic(u'time sc = pl.map(scrape, urls)')
data = [s for s in sc if s]
pl.terminate()
print "exported %d articles" %len(data)


# In[6]:

f = open('out.json','w')
f.write(json.dumps(data, ensure_ascii=False, indent=2))
f.close()


# In[ ]:



