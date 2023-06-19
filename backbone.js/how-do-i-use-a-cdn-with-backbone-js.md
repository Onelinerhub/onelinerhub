# How do I use a CDN with Backbone.js?
// plain

Backbone.js is a JavaScript library that allows developers to create single-page applications. A CDN (Content Delivery Network) is a network of servers that deliver web content to users based on their geographic location.

Using a CDN with Backbone.js is relatively simple. First, include the Backbone.js library from a CDN in your HTML file:

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.3.3/backbone-min.js"></script>
```

This will allow the browser to retrieve the Backbone.js library from the CDN instead of your local server.

Next, you can include any additional Backbone.js components from the same CDN. For example, to include the Backbone.LocalStorage library from the same CDN, you can use the following code:

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/backbone-localstorage.js/1.1.16/backbone.localStorage-min.js"></script>
```

Finally, you can use the Backbone.js library and components in your code as you would normally.

## Helpful links
- https://cdnjs.com/libraries/backbone.js/
- https://cdnjs.com/libraries/backbone-localstorage.js/

onelinerhub: [How do I use a CDN with Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-use-a-cdn-with-backbone-js)