# How do I remove a model attribute using Backbone.js?
// plain

To remove a model attribute using Backbone.js, you can use the `unset()` method. This method takes a single parameter, which is the attribute name to be removed from the model instance.

For example, if you have a model instance with the attributes `name` and `age`, you can remove the `name` attribute with the following code:

```javascript
model.unset('name');
```

This will remove the `name` attribute from the model instance.

## Code explanation

- `model` - a model instance
- `unset()` - a method of the model instance that takes a single parameter, which is the attribute name to be removed
- `'name'` - the attribute name to be removed

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/#Model-unset)

onelinerhub: [How do I remove a model attribute using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-remove-a-model-attribute-using-backbone-js)