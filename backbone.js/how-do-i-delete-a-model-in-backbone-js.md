# How do I delete a model in Backbone.js?
// plain

To delete a model in Backbone.js, you can use the `destroy` method. This method will remove the model from the server as well as from the collection.

## Example code

```
var model = new Backbone.Model({
  name: 'John Doe'
});

model.destroy({
  success: function(model, response) {
    console.log('Model deleted!');
  },
  error: function(model, response) {
    console.log('An error occurred!');
  }
});
```
## Output example
 `Model deleted!`

The code above will delete the model from the server and from the collection. The `success` and `error` callbacks will be triggered depending on the result of the `destroy` method.

## Code explanation

- `var model = new Backbone.Model({name: 'John Doe'});` - create a new model
- `model.destroy({...})` - call the destroy method on the model
- `success` - callback to be triggered if the delete is successful
- `error` - callback to be triggered if the delete is not successful

## Helpful links
- [Backbone.js Documentation - Model.destroy](http://backbonejs.org/#Model-destroy)
- [Backbone.js Tutorials - Deleting a Model](https://www.tutorialspoint.com/backbonejs/backbonejs_deleting_a_model.htm)

onelinerhub: [How do I delete a model in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-delete-a-model-in-backbone-js)