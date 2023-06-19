# How do I use an interval in AngularJS?
// plain

An interval in AngularJS is a time based function that is used to schedule tasks to run at a certain time. It can be used to create a timer, or to execute a function at a certain time interval.

## Example code

```
// Create the interval
$interval(function() {
  console.log("Hello World!");
}, 1000);
```

## Output example

```
Hello World!
Hello World!
Hello World!
...
```

The code above will print "Hello World!" every one second.

## Code explanation

- `$interval` is the AngularJS service used to create an interval.
- The first argument is the function to be executed.
- The second argument is the time interval in milliseconds.

## Helpful links
- [AngularJS $interval Documentation](https://docs.angularjs.org/api/ng/service/$interval)

onelinerhub: [How do I use an interval in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-an-interval-in-angularjs)