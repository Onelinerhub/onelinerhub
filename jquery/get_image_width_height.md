# Get image width and height

```javascript
$('<img/>').attr('src', 'https://via.placeholder.com/300.png').load(function() {
  console.log( this.width + 'x' + this.height );
});
```

- $('<img/\>') - creates virtual ```img``` element
- 300.png - sample image URL
- this.width + 'x' + this.height - will print ```300x300``` for selected image
