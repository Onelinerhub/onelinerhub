# How do I make a POST request using Backbone.js?
// plain

A POST request can be made using Backbone.js by creating a model instance and calling the save() method. The save() method sends an HTTP POST request to the server with the model's attributes.

## Example

```js
var user = new Backbone.Model({
    name: "John Doe"
});

user.save(null, {
    success: function(model, response, options) {
        console.log("POST request successful");
    },
    error: function(model, response, options) {
        console.log("POST request failed");
    }
});
```

## Output example

```
POST request successful
```

## Code explanation

- `var user = new Backbone.Model({name: "John Doe"});`: creates a new model instance with the attribute `name` set to `John Doe`
- `user.save(null, {...});`: calls the save() method on the model instance which will send an HTTP POST request to the server
- `success` and `error` callbacks: callbacks that will be called depending on the response from the server

## Helpful links
- [Backbone.Model.save()](http://backbonejs.org/#Model-save)
- [Backbone.sync()](http://backbonejs.org/#Sync)

onelinerhub: [How do I make a POST request using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-make-a-post-request-using-backbone-js)