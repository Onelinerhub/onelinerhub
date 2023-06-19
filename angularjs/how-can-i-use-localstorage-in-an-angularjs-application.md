# How can I use localstorage in an AngularJS application?
// plain

Localstorage is a great way to store information in an AngularJS application. It is a key-value pair storage system that allows you to store data in the browser that will persist even after the page is refreshed.

To use localstorage in an AngularJS application, you can use the `$window` service. This service provides access to the `localStorage` property, which is an object that allows you to store data.

## Example code

```javascript
// Store data in localStorage
$window.localStorage.setItem('key', 'value');

// Retrieve data from localStorage
var data = $window.localStorage.getItem('key');
```

## Output example
 `null`

The code above stores a key-value pair in localStorage and retrieves the value stored in that key.

## Code explanation

- `$window`: This is the AngularJS service that provides access to the `localStorage` property.
- `localStorage`: This is the object that allows you to store data in the browser.
- `setItem()`: This is the method used to store data in localStorage.
- `getItem()`: This is the method used to retrieve data from localStorage.

List of ## Helpful links
- [AngularJS Documentation for $window](https://docs.angularjs.org/api/ng/service/$window)
- [MDN Documentation for localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

onelinerhub: [How can I use localstorage in an AngularJS application?](https://onelinerhub.com/angularjs/how-can-i-use-localstorage-in-an-angularjs-application)