# How do I use jQuery to modify an HTML element's href attribute?
// plain

To modify an HTML element's href attribute using jQuery, you can use the `attr()` method. This method takes two parameters, the first being the name of the attribute you want to modify and the second being the new value you want to set it to. For example, the following code block would change the href attribute of the element with the ID `myLink` to `https://www.example.com`:
```javascript
$('#myLink').attr('href', 'https://www.example.com');
```

The `attr()` method can also be used to retrieve the current value of an attribute. To do this, you only need to pass the attribute name as the parameter. For example, the following code block would return the current href value of the element with the ID `myLink`:
```javascript
var hrefValue = $('#myLink').attr('href');
// hrefValue will now contain the current href value
```

The `attr()` method is part of the jQuery core library and is available for use in all versions of jQuery.

#### List of code parts with detailed explanation
- `$('#myLink')`: This is a jQuery selector used to select the element with the ID `myLink`.
- `attr('href')`: This is the `attr()` method used to either modify or retrieve the value of the href attribute.
- `attr('href', 'https://www.example.com')`: This is the `attr()` method used to set the href attribute to the new value `https://www.example.com`.

#### List of relevant links
- [jQuery attr() documentation](https://api.jquery.com/attr/)

onelinerhub: [How do I use jQuery to modify an HTML element's href attribute?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-modify-an-html-element-s-href-attribute)