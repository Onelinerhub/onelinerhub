# How do I use Angular Zone to detect and run Angular change detection?
// plain

A Zone is an execution context that allows us to detect and run Angular change detection. It is an execution context that allows us to detect and run Angular change detection. It is an execution context that allows us to detect and run Angular change detection.

To use Angular Zone to detect and run Angular change detection, we can use the NgZone service. This service provides a run() method which allows us to run a callback function inside the Angular Zone. The run() method takes a callback function and an optional context object as parameters.

## Example code

```
constructor(private zone: NgZone) {
  this.zone.run(() => {
    // Do something in Angular Zone
  });
}
```

The run() method will execute the callback function inside the Angular Zone and will trigger change detection. This allows us to detect and run Angular change detection whenever the callback is executed.

## Code explanation

- `constructor(private zone: NgZone)`: This injects the NgZone service into the constructor.
- `this.zone.run(() => {`: This is the run() method of the NgZone service which takes a callback function as parameter.
- `// Do something in Angular Zone`: This is the callback function which will be executed inside the Angular Zone.
- `});`: This is the closing bracket of the run() method.

## Helpful links
- [Angular Documentation: NgZone](https://angular.io/api/core/NgZone)
- [Angular Documentation: Zones](https://angular.io/guide/zones)

onelinerhub: [How do I use Angular Zone to detect and run Angular change detection?](https://onelinerhub.com/angularjs/how-do-i-use-angular-zone-to-detect-and-run-angular-change-detection)