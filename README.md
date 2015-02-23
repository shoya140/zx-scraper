zx-scraper
======================

[scraping.ipynb](http://nbviewer.ipython.org/github/shoya140/zx-scraper/blob/master/scraping.ipynb)

### data structure

```
{
  'url': url,
  'title': title,
  'description': description,
  'image': image(optional),
  'articles': [
    {
      'title': title(optional),
      'text': text(optional),
      'column': column(optional),
      'images': [
        image(optional),
      ],
      'photo_read': photo_read(optional),
      'price': price(optional)
    },
  ],
  'tags': [
    tag(optional),
  ]
}