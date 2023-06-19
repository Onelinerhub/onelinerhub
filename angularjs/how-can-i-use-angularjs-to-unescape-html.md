# How can I use AngularJS to unescape HTML?
// plain

AngularJS provides a built-in filter called `$sce` (Strict Contextual Escaping) that can be used to unescape HTML. This filter is available through the `$filter` service.

To use `$sce`, you must first inject the `$filter` service into your controller, directive, or service.

```
// Inject the $filter service
function MyController($filter) {
  // Get the $sce filter
  var sce = $filter('$sce');

  // Unescape HTML
  var unescapedHtml = sce.trustAsHtml('<p>This is escaped HTML</p>');
}
```

The output of the code above is `<p>This is escaped HTML</p>` (unescaped HTML).

The `$sce` filter has two methods that can be used to unescape HTML: `trustAsHtml` and `trustAsResourceUrl`.

- `trustAsHtml`: This method takes a string as an argument and returns the unescaped version of the string.
- `trustAsResourceUrl`: This method takes a URL as an argument and returns the unescaped version of the URL.

For more information about `$sce`, please see the [AngularJS documentation](https://docs.angularjs.org/api/ng/service/$sce).

onelinerhub: [How can I use AngularJS to unescape HTML?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-unescape-html)