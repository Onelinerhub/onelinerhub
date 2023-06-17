# How can I prevent jQuery XSS vulnerabilities?
// plain

1. Use the jQuery .html() or .text() method to sanitize user input. This will ensure that any malicious code is removed before it is rendered in the browser.

```
var userInput = '<script>alert("XSS attack!")</script>';
$('#userInput').html(userInput);
```

2. Use the jQuery .attr() method to set attributes on elements. This will ensure that any malicious code is removed before it is rendered in the browser.

```
var userInput = '<script>alert("XSS attack!")</script>';
$('#userInput').attr('title', userInput);
```

3. Use the jQuery .data() method to set data attributes on elements. This will ensure that any malicious code is removed before it is rendered in the browser.

```
var userInput = '<script>alert("XSS attack!")</script>';
$('#userInput').data('userInput', userInput);
```

4. Use the jQuery .removeData() method to remove data attributes from elements. This will ensure that any malicious code is removed before it is rendered in the browser.

```
$('#userInput').removeData('userInput');
```

5. Use the jQuery .replaceWith() method to replace elements with sanitized content. This will ensure that any malicious code is removed before it is rendered in the browser.

```
var userInput = '<script>alert("XSS attack!")</script>';
$('#userInput').replaceWith('<div>' + userInput + '</div>');
```

6. Use the jQuery .on() method to bind events to elements. This will ensure that any malicious code is not executed when the event is triggered.

```
$('#userInput').on('click', function(){
    alert('XSS prevented!');
});
```

7. Use the jQuery .off() method to unbind events from elements. This will ensure that any malicious code is not executed when the event is triggered.

```
$('#userInput').off('click');
```

## Helpful links
- [jQuery XSS Prevention](https://www.sitepoint.com/jquery-xss-prevention/)
- [jQuery Security Cheat Sheet](https://www.owasp.org/index.php/jQuery_Security_Cheat_Sheet)

onelinerhub: [How can I prevent jQuery XSS vulnerabilities?](https://onelinerhub.com/jquery/how-can-i-prevent-jquery-xss-vulnerabilities)