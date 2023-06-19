# How can I create a model with Backbone.js?
// plain

Backbone.js is a JavaScript library that provides structure to web applications by providing models with key-value binding and custom events. To create a model with Backbone.js, you need to first create a Model class. You can do this by extending the Backbone.Model class.

```
var MyModel = Backbone.Model.extend({
    defaults: {
        name: 'John Doe',
        age: 25
    },
    initialize: function(){
        console.log("Model initialized!");
    }
});

var myModel = new MyModel();

console.log(myModel.get('name'));
// Output: John Doe
```

In the example above, we created a Model class named MyModel that extends the Backbone.Model class. We then added a defaults object which contains two key-value pairs. We also added an initialize function that will be called when the model is instantiated. Finally, we created an instance of the model and used the get() method to retrieve the name property from the model.

## Code explanation


1. var MyModel = Backbone.Model.extend({...}: This creates a Model class named MyModel that extends the Backbone.Model class.
2. defaults: {name: 'John Doe', age: 25}: This adds a defaults object to the model that contains two key-value pairs.
3. initialize: function(){console.log("Model initialized!");}: This adds an initialize function to the model that will be called when the model is instantiated.
4. var myModel = new MyModel(): This creates an instance of the model.
5. myModel.get('name'): This uses the get() method to retrieve the name property from the model.

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Getting Started with Backbone.js](https://scotch.io/tutorials/getting-started-with-backbone-js)

onelinerhub: [How can I create a model with Backbone.js?](https://onelinerhub.com/backbone.js/how-can-i-create-a-model-with-backbone-js)