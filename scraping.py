
# coding: utf-8

# In[1]:



import json
import urllib
from bs4 import BeautifulSoup
from multiprocessing import Pool

base_url = 'http://zexy.net'


# In[2]:

def clean(string):
    return string.strip().replace('\n', '').replace('\t', '').encode('utf-8')

def scrape(url):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html)
    contents = soup.find('div', attrs={'id':'contents'})
    if not contents:
        return
    
    # main
    main = soup.find('article',attrs={'id':'h1_box'})
    title = main.find('h1')
    description = main.find('p')
    data = {
        'url': url,
        'title': clean(title.text),
        'description': clean(description.text)
    }
    image_section = main.find('section', attrs={'class':'main_img'})
    if image_section:
        image = image_section.find('img')
        data.update({'image': clean(base_url + image['src'])})

    # tags
    tag = soup.find('ul', attrs={'class':'tag_icon'})
    tags = tag.findAll('li')
    data.update({'tags':[clean(x.text) for x in tags]})
    
    # articles
    articles = soup.findAll('article', attrs={'class':['', 'no_s']})
    da = []
    for article in articles:
        d = {}
        title = article.find('h2')
        if title:
            d.update({'title':clean(title.text)})
        image = article.find('img')
        if image: 
            d.update({'image': clean(base_url + image['src'])})
        text = article.find('p', attrs={'class':'item1_text'})
        if text: 
            d.update({'text':clean(text.text)})
        column = article.find('section', attrs={'class':'column'})
        if column: 
            d.update({'column':clean(column.text)})
        da.append(d)
    data.update({'articles':da})

    return data


# In[3]:

urls = ['http://zexy.net/article/app%09d' %i for i in range(0, 100)]
pl = Pool()
get_ipython().magic(u'time sc = pl.map(scrape, urls)')
data = [s for s in sc if s]
pl.terminate()
print "exported %d articles" % len(data)


# In[4]:

f = open('out.json','w')
f.write(json.dumps(data, ensure_ascii=False, indent=2))
f.close()


# In[ ]:



