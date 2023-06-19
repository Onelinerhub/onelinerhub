# How do I use Angular Zone to run my code?
// plain

Angular Zone is a library that allows you to run your code inside a zone, which is a special context that allows you to detect when asynchronous tasks are running and when they are completed.

To use Angular Zone, you need to import it into your application.

```
import { NgZone } from '@angular/core';
```

Then, you can create a new zone instance and use it to run your code.

```
const zone = new NgZone({ enableLongStackTrace: false });

zone.run(() => {
  // Your code here
});
```

The `run()` method takes a function as a parameter and executes it in the zone context. Inside the function, you can write your own code, such as making an API call or updating a variable.

You can also use the `runOutsideAngular()` method to run code outside of the zone context. This is useful if you need to run code that doesn't need to be tracked by the zone.

```
zone.runOutsideAngular(() => {
  // Your code here
});
```

Finally, you can use the `onStable` method to detect when all asynchronous tasks have been completed.

```
zone.onStable.subscribe(() => {
  console.log('All asynchronous tasks have been completed');
});
```

## Output example

```
All asynchronous tasks have been completed
```

## Helpful links
- [Angular Zone Documentation](https://angular.io/api/core/NgZone)

onelinerhub: [How do I use Angular Zone to run my code?](https://onelinerhub.com/angularjs/how-do-i-use-angular-zone-to-run-my-code)