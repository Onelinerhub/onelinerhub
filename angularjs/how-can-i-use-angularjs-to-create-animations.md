# How can I use AngularJS to create animations?
// plain

AngularJS provides a powerful animation framework that can be used to create complex animations. The ngAnimate module provides support for CSS-based animations (keyframes and transitions) as well as JavaScript-based animations.

To create an animation using AngularJS, you need to include the ngAnimate module as a dependency in your application.

```
angular.module('myApp', ['ngAnimate']);
```

You can then define the animation in the CSS using keyframes or transitions.

```
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

.fade-in {
  animation: fadeIn 2s;
}
```

You can then apply the animation to an element by adding the `fade-in` class to the element.

```
<div class="fade-in">This element will fade in</div>
```

The animation can be further customized by using the `$animate` service in the controller. The `$animate` service provides methods for triggering the animation, setting the duration, and adding a callback function.

```
$animate.addClass(element, 'fade-in', {
  duration: 1000,
  done: function(){
    // do something when the animation is complete
  }
});
```

The animation can also be triggered by events in the controller.

```
$scope.openModal = function(){
  $animate.addClass(element, 'fade-in', {
    duration: 1000
  });
}
```

For more information on creating animations with AngularJS, see the [AngularJS Documentation](https://docs.angularjs.org/guide/animations).

onelinerhub: [How can I use AngularJS to create animations?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-create-animations)