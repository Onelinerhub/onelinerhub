# How do I use AngularJS to zoom in on an image?
// plain

To use AngularJS to zoom in on an image, you can use the [ng-zoom](https://github.com/visme/ng-zoom) directive. This directive takes an image URL and a zoom factor as parameters and then creates an interactive zoomable image.

## Example code

```
<ng-zoom image="imageURL" zoom-factor="2"></ng-zoom>
```

This code will create an image with the given URL that can be zoomed in by a factor of 2.

The code consists of the following parts:
- `ng-zoom`: This is the directive that is used to create the zoomable image.
- `image`: This is the parameter that takes the URL of the image to be zoomed.
- `zoom-factor`: This is the parameter that takes the zoom factor as an input.

## Helpful links
- https://github.com/visme/ng-zoom
- https://docs.angularjs.org/guide/directive

onelinerhub: [How do I use AngularJS to zoom in on an image?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-zoom-in-on-an-image)