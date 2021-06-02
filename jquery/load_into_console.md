# Load jQuery into console for any website

```javascript
(function(e, s) {
    e.src = s;
    e.onload = function() {
        jQuery.noConflict();
        console.log('jQuery loaded into console');
    };
    document.head.appendChild(e);
})(document.createElement('script'), '//code.jquery.com/jquery-latest.min.js')
```

- document.createElement('script') - creates script element
- \/\/code.jquery.com\/jquery-latest.min.js - path to the latest jQuery CDN
- jQuery.noConflict() - uses safe mode without ```$``` function (use ```jQuery``` function instead, which is an alias of ```$```)
- document.head.appendChild - inserts jQuery into current web page
