# How can I use JavaScript to access Polymer properties?
// plain

You can use JavaScript to access Polymer properties by using the `Polymer.dom()` API. This API provides access to the properties of the Polymer element.

For example, to access the `name` property of a Polymer element:

```
let name = Polymer.dom(this).name;
```

The `Polymer.dom()` API takes two arguments:

1. `this`: This is the context in which the API is called. In this case, it is the Polymer element itself.
2. `name`: This is the name of the property that you want to access.

The output of the above code will be the value of the `name` property.

You can also use the `Polymer.dom()` API to access other properties of the Polymer element such as `id`, `className`, `style`, and so on.

## Helpful links
- [Polymer.dom() API](https://www.polymer-project.org/3.0/docs/devguide/local-dom#polymer-dom)
- [Accessing Polymer Element Properties](https://www.polymer-project.org/3.0/docs/devguide/local-dom#accessing-polymer-element-properties)

onelinerhub: [How can I use JavaScript to access Polymer properties?](https://onelinerhub.com/javascript-polymer/how-can-i-use-javascript-to-access-polymer-properties)