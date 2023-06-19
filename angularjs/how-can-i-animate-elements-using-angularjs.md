# How can I animate elements using AngularJS?
// plain

Animate elements using AngularJS is quite easy. First, you need to include the `ngAnimate` module in your application.

```
angular.module('myApp', ['ngAnimate'])
```

Then, you need to add the `ng-animate` class to the elements you want to animate.

```
<div class="my-class ng-animate"></div>
```

Finally, you need to add the animation styles to the CSS file.

```
.my-class.ng-enter {
  opacity: 0;
  transition: 0.5s linear all;
}

.my-class.ng-enter.ng-enter-active {
  opacity: 1;
}
```

In this example, when the element with the `my-class` class is added to the DOM, it will fade in.

## Code explanation


* `angular.module('myApp', ['ngAnimate'])` - This line adds the `ngAnimate` module to the application.

* `<div class="my-class ng-animate"></div>` - This line adds the `ng-animate` class to the element.

* `.my-class.ng-enter { opacity: 0; transition: 0.5s linear all; }` - This line sets the initial style of the element.

* `.my-class.ng-enter.ng-enter-active { opacity: 1; }` - This line sets the final style of the element.

## Helpful links

* [Angular Animations Guide](https://angular.io/guide/animations)
* [ngAnimate API Reference](https://docs.angularjs.org/api/ngAnimate)

onelinerhub: [How can I animate elements using AngularJS?](https://onelinerhub.com/angularjs/how-can-i-animate-elements-using-angularjs)