# How do I set a timeout in AngularJS?
// plain

In AngularJS, the $timeout service is used to set a timeout. This service is a wrapper around the window.setTimeout function and provides a way to execute code after a given time interval.

The syntax for using the $timeout service is as follows:

```
$timeout(function(){
    // code to execute
}, time_in_ms);
```

Where `time_in_ms` is the time in milliseconds after which the code should be executed.

For example, the following code will execute a function after 1 second:

```
$timeout(function(){
    console.log("Executing after 1 second");
}, 1000);

// Output: Executing after 1 second
```

The $timeout service also provides a way to cancel a timeout by calling the cancel() method on the promise that is returned by the $timeout service.

For example, the following code will cancel a timeout after 1 second:

```
var promise = $timeout(function(){
    console.log("Executing after 1 second");
}, 1000);

promise.cancel();
```

## Helpful links
- [AngularJS Documentation - $timeout](https://docs.angularjs.org/api/ng/service/$timeout)

onelinerhub: [How do I set a timeout in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-set-a-timeout-in-angularjs)