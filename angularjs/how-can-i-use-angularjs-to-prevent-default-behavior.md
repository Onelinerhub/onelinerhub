# How can I use AngularJS to prevent default behavior?
// plain

AngularJS provides a few different ways to prevent default behavior.

1. Using `ng-click` Directive:

`ng-click` directive allows us to prevent default behavior of an element. We can use `$event.preventDefault()` to prevent the default behavior.

For example:
```
<a href="www.example.com" ng-click="$event.preventDefault()">Link</a>
```

2. Using `$event` Object:

We can also use `$event` object to prevent default behavior of an element. We can use `$event.preventDefault()` to prevent the default behavior.

For example:
```
<a href="www.example.com" ng-click="doSomething($event)">Link</a>

<script>
  $scope.doSomething = function($event) {
    $event.preventDefault();
  }
</script>
```

3. Using `$event.stopPropagation()`:

`$event.stopPropagation()` can be used to prevent event bubbling.

For example:
```
<div ng-click="doSomething($event)">
  <a href="www.example.com" ng-click="$event.stopPropagation()">Link</a>
</div>

<script>
  $scope.doSomething = function($event) {
    console.log('This will not be called');
  }
</script>
```

## Helpful links

- [ng-click Directive](https://docs.angularjs.org/api/ng/directive/ngClick)
- [AngularJS Event Model](https://docs.angularjs.org/guide/expression#-event-)

onelinerhub: [How can I use AngularJS to prevent default behavior?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-prevent-default-behavior)