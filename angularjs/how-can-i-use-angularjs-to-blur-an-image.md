# How can I use AngularJS to blur an image?
// plain

Using AngularJS, we can blur an image by applying a filter to it. To do this, we can use the `ng-style` directive. This directive allows us to set the style attribute of an element dynamically. We can use it to set the `filter` property of an element to `blur(px)`, where `px` is the amount of blur to apply.

```html
<img ng-src="{{myImageUrl}}" ng-style="{'filter': 'blur(3px)'}" />
```

This will blur the image by 3px.

The code above consists of the following parts:

* `<img>`: The HTML element to which the filter will be applied.
* `ng-src`: The AngularJS directive that will bind the element to the `myImageUrl` variable.
* `ng-style`: The AngularJS directive that will set the style attribute of the element.
* `filter`: The CSS property that will be used to apply the blur filter.
* `blur(px)`: The value of the `filter` property, where `px` is the amount of blur to apply.

## Helpful links

* [ng-style](https://docs.angularjs.org/api/ng/directive/ngStyle)
* [CSS filter property](https://developer.mozilla.org/en-US/docs/Web/CSS/filter)

onelinerhub: [How can I use AngularJS to blur an image?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-blur-an-image)