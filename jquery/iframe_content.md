# Access iframe content

```javascript
$('iframe').contents().find('div');
```

- $('iframe') - jQuery selector for needed iframe
- contents() - will return jquery content wrapper (respect [same origin](https://en.wikipedia.org/wiki/Same-origin_policy) for this to work)
- find('div') - example of selecting first ```div``` element inside chosen iframe (you can use any kind of jquery functions here)
