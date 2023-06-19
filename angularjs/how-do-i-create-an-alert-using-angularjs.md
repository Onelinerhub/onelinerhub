# How do I create an alert using AngularJS?
// plain

To create an alert using AngularJS, you can use the `$window.alert()` method. This method takes in a single string argument, which will be displayed in the alert window.

For example:
```
$window.alert('This is an alert!');
```
## Output example

```
This is an alert!
```

The code above will create a popup alert window with the message `This is an alert!`.

The `$window.alert()` method has two parts:
- `$window`: This is an AngularJS service that provides an API to interact with the browser's window object.
- `alert()`: This is a method of the window object that takes a string argument, and displays it in an alert window.

For more information on the `$window` service, please see the [AngularJS documentation](https://docs.angularjs.org/api/ng/service/$window).

onelinerhub: [How do I create an alert using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-an-alert-using-angularjs)