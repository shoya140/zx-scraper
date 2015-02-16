zx-scraper
======================

### data structure

```
{
  'url': url,
  'title': title,
  'description': rescription,
  'image': image(optional),
  'articles': [
    {
      'title': title(optional),
      'image': image(optional),
      'text': text,
      'column': column
    },
  ],
  'tags': [
    'tag':tag,
  ]
}