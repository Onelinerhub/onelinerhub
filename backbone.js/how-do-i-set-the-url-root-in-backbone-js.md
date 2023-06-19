# How do I set the URL root in Backbone.js?
// plain

To set the URL root in Backbone.js, you can use the `root` property of the `Backbone.History` object. This allows you to set the root URL for all subsequent requests.

For example:
```
Backbone.history.root = "/my/app/";
```

This will set the root URL for all subsequent requests to `/my/app/`.

The parts of this code are as follows:

- `Backbone.history.root`: The `root` property of the `Backbone.History` object.
- `/my/app/`: The URL you are setting as the root URL for all subsequent requests.

## Helpful links
- [Backbone.History](http://backbonejs.org/#History)
- [Backbone.js Documentation](http://backbonejs.org/)

onelinerhub: [How do I set the URL root in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-set-the-url-root-in-backbone-js)