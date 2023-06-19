# How can I use Angular to zoom in on an image?
// plain

Angular provides the ability to zoom in on an image using the `transform` property. This property allows you to scale, rotate, and skew elements. To zoom in on an image, you can use the `scale` function.

```
<img src="image.jpg" [style.transform]="'scale(2)'" />
```

This code example will double the size of the image. To increase the zoom level, you can increase the number in the scale function.

## Code explanation


* `<img src="image.jpg"` - This part of the code specifies the image to be zoomed in on.
* `[style.transform]="'scale(2)'"` - This part of the code specifies the `transform` property and the `scale` function with a value of 2. This will double the size of the image.

## Helpful links
* [Angular Documentation - Styling](https://angular.io/guide/styling)
* [MDN Web Docs - transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

onelinerhub: [How can I use Angular to zoom in on an image?](https://onelinerhub.com/angularjs/how-can-i-use-angular-to-zoom-in-on-an-image)