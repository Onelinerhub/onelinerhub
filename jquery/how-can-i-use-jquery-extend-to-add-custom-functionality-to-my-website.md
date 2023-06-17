# How can I use jQuery extend to add custom functionality to my website?
// plain

You can use jQuery extend to add custom functionality to your website by extending the jQuery object. This allows you to create custom functions that can be used in your website. For example, you can create a custom function to add a class to an element:

```
$.extend({
  addClass: function(el, className) {
    $(el).addClass(className);
  }
});

// Usage
$.addClass('#myElement', 'active');
```

This will add the class `active` to the element with the id `myElement`.

## Code explanation


1. `$.extend({ ... });` - This creates a new jQuery function that can be used in your website.
2. `addClass: function(el, className) { ... }` - This is the custom function you created. It takes two parameters, `el` and `className`.
3. `$(el).addClass(className);` - This calls the [`addClass()`](https://api.jquery.com/addClass/) jQuery function to add the class to the element.

## Helpful links

- [jQuery extend](https://api.jquery.com/jQuery.extend/)
- [addClass()](https://api.jquery.com/addClass/)

onelinerhub: [How can I use jQuery extend to add custom functionality to my website?](https://onelinerhub.com/jquery/how-can-i-use-jquery-extend-to-add-custom-functionality-to-my-website)