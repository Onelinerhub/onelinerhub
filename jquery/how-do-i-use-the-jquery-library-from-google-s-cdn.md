# How do I use the jQuery library from Google's CDN?
// plain

To use the jQuery library from Google's CDN, you need to include the following HTML tag in the `<head>` section of your HTML document:

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
```

This tag links the jQuery library from Google's CDN to the HTML document.

Once the library is linked, you can use the jQuery library in your JavaScript code. For example, the following code will select all `<p>` elements and change their background color to red:

```javascript
$('p').css('background-color', 'red');
```

## Code explanation


- `$('p')`: Selects all `<p>` elements
- `.css('background-color', 'red')`: Sets the background color of the selected elements to red

This code will result in all `<p>` elements having a red background color.

## Helpful links

- [Google Hosted Libraries - jQuery](https://developers.google.com/speed/libraries/#jquery)
- [jQuery API Documentation](https://api.jquery.com/)

onelinerhub: [How do I use the jQuery library from Google's CDN?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-library-from-google-s-cdn)