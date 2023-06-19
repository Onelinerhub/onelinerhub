# How do I open a link in a new tab using AngularJS?
// plain

You can open a link in a new tab using AngularJS by using the `$window.open()` method. This method takes two parameters, the first being the URL of the link you want to open and the second being the target of the link. To open in a new tab, set the second parameter to `_blank`. Here is an example:

```
$window.open('https://www.google.com', '_blank');
```

This will open a new tab in the browser and load the URL provided in the first parameter.

The `$window.open()` method is part of the `$window` service, which is provided by AngularJS. The `$window` service is a reference to the browser's `window` object, and provides access to most of the browser's features.

Here is a list of the parts of the code and their explanation:

- `$window.open()`: The method that is used to open a link in a new tab.
- `https://www.google.com`: The URL of the link you want to open.
- `_blank`: The target of the link, set to `_blank` to open in a new tab.

## Helpful links

- [AngularJS $window Service Documentation](https://docs.angularjs.org/api/ng/service/$window)

onelinerhub: [How do I open a link in a new tab using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-open-a-link-in-a-new-tab-using-angularjs)