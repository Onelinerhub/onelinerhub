# How do I copy an element in AngularJS?
// plain

In AngularJS, you can copy an element using the `angular.copy()` method. This method takes two parameters - the source element and the destination element. The source element is the element that you want to copy and the destination element is the element that you want to copy the source element to.

For example, if we have a source element `myObject` and a destination element `myCopy`, we can use the following code to copy the source element to the destination element:

```javascript
var myObject = {
  name: 'John',
  age: 30
};

var myCopy = {};

angular.copy(myObject, myCopy);

console.log(myCopy);
// Output: {name: 'John', age: 30}
```

The code above has the following parts:

1. `myObject` - the source element that we want to copy.
2. `myCopy` - the destination element that we want to copy the source element to.
3. `angular.copy(myObject, myCopy)` - the method used to copy the source element to the destination element.
4. `console.log(myCopy)` - the output of the copied source element.

For more information on the `angular.copy()` method, please refer to the [AngularJS API reference](https://docs.angularjs.org/api/ng/function/angular.copy).

onelinerhub: [How do I copy an element in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-copy-an-element-in-angularjs)