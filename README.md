zx-scraper
======================

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