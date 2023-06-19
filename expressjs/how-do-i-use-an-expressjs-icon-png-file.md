# How do I use an expressjs icon PNG file?
// plain

Using a PNG file with expressjs is a simple process.

1. First, place the PNG file in the public folder of your expressjs application.

2. Then, in the HTML file where you want to display the icon, include the following code:
```
<img src="/path/to/image.png" alt="icon">
```
This code will render the image on the page.

3. To adjust the size of the image, use the `width` and `height` attributes:
```
<img src="/path/to/image.png" alt="icon" width="50" height="50">
```
This code will render an image that is 50px by 50px.

4. To add a link to the icon, wrap the `img` tag in an `a` tag:
```
<a href="https://www.example.com">
  <img src="/path/to/image.png" alt="icon" width="50" height="50">
</a>
```
This code will render a link to `https://www.example.com` when the icon is clicked.

5. To add a hover effect to the icon, use the `:hover` pseudo-class:
```
<a href="https://www.example.com" class="icon">
  <img src="/path/to/image.png" alt="icon" width="50" height="50"
    onmouseover="this.src='/path/to/other-image.png'"
    onmouseout="this.src='/path/to/image.png'">
</a>
```
This code will render a different image when the user hovers over the icon.

## Helpful links
- [Express.js](https://expressjs.com/)
- [HTML img tag](https://www.w3schools.com/tags/tag_img.asp)
- [CSS Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

onelinerhub: [How do I use an expressjs icon PNG file?](https://onelinerhub.com/expressjs/how-do-i-use-an-expressjs-icon-png-file)