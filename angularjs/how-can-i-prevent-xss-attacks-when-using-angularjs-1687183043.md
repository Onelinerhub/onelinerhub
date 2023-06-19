# How can I prevent XSS attacks when using AngularJS?
// plain

To prevent XSS attacks when using AngularJS, you should:

1. **Sanitize user input:** Use the `$sanitize` service to sanitize all user input before it is displayed in the view. For example:

```javascript
var userInput = $sanitize(userInput);
```

2. **Encode user input:** You can use the `$sce` service to encode user input. This will ensure that any malicious code is rendered as text and not as HTML. For example:

```javascript
var userInput = $sce.trustAsHtml(userInput);
```

3. **Disable HTML in bindings:** Use the `ng-bind-html` attribute to disable HTML in bindings. This will prevent malicious code from being executed. For example:

```html
<div ng-bind-html="userInput"></div>
```

4. **Disable unsafe JavaScript:** Use the `ng-non-bindable` attribute to disable unsafe JavaScript in bindings. This will prevent malicious code from being executed. For example:

```html
<div ng-non-bindable="userInput"></div>
```

5. **Validate user input:** Validate user input to ensure that it does not contain malicious code. You can use the `$filter` service to validate user input. For example:

```javascript
var userInput = $filter('validateInput')(userInput);
```

For more information, please see the [AngularJS Security Guide](https://docs.angularjs.org/guide/security).

onelinerhub: [How can I prevent XSS attacks when using AngularJS?](https://onelinerhub.com/angularjs/how-can-i-prevent-xss-attacks-when-using-angularjs-1687183043)