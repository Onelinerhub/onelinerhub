# model

How do I define a model in Backbone.js?
// plain

A model in Backbone.js is an object that contains data for an application. It is the core of the framework for representing data and business logic. Models are used to store and retrieve data from the server, and to monitor changes to the data.

## Example code

```
var TaskModel = Backbone.Model.extend({
    defaults: {
        title: '',
        completed: false
    },
    validate: function(attrs) {
        if (_.isEmpty(attrs.title)) {
            return 'Title is required';
        }
    },
    toggle: function() {
        this.set('completed', !this.get('completed'));
    }
});

var task = new TaskModel({
    title: 'My Task'
});

console.log(task.get('title')); // 'My Task'
console.log(task.get('completed')); // false
```

## Output example

```
My Task
false
```

The code above defines a model called TaskModel that extends the Backbone.Model class. It has two attributes, title and completed, and a validate method that checks if the title is set. The toggle method sets the completed attribute to the opposite of its current value. The last line creates an instance of the model and sets the title attribute.

Parts of the code:
- `var TaskModel = Backbone.Model.extend({`: This line creates a new model called TaskModel that extends the Backbone.Model class.
- `defaults: {`: This is the object that contains the default values for the model's attributes.
- `validate: function(attrs) {`: This is the validate method that checks if the title attribute is set.
- `toggle: function() {`: This is the toggle method that sets the completed attribute to the opposite of its current value.
- `var task = new TaskModel({`: This line creates an instance of the model and sets the title attribute.

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/)
- [Models](http://backbonejs.org/#Model)

onelinerhub: [model

How do I define a model in Backbone.js?](https://onelinerhub.com/backbone.js/model--how-do-i-define-a-model-in-backbone-js)