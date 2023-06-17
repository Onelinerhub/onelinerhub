# How do I use jQuery's noconflict mode?
// plain

jQuery's noconflict mode is a way to avoid conflicts between different versions of jQuery and other libraries that use the same variable names. It allows you to use multiple versions of jQuery on the same page without causing conflicts.

To use jQuery's noconflict mode, you must first assign the jQuery object to a different variable name. Here is an example:

```javascript
var jq = $.noConflict();
```

This will assign the jQuery object to the variable `jq`, and the `$` variable will no longer refer to jQuery.

You can then use the `jq` variable instead of `$` when you call jQuery functions. For example:

```javascript
jq(document).ready(function() {
  jq("div").hide();
});
```

This will hide all `div` elements on the page.

To learn more about jQuery's noconflict mode, see the following links:

* [jQuery noConflict() Method](https://www.w3schools.com/jquery/jquery_noconflict.asp)
* [Using jQuery noConflict()](https://api.jquery.com/jquery.noconflict/)

onelinerhub: [How do I use jQuery's noconflict mode?](https://onelinerhub.com/jquery/how-do-i-use-jquery-s-noconflict-mode)