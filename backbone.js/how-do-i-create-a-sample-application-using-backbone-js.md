# How do I create a sample application using Backbone.js?
// plain

Creating a sample application using Backbone.js involves several steps.

1. Include the Backbone.js library in the HTML file.
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.3.3/backbone-min.js"></script>
```
2. Create a model to define the data structure for the application.
```
var Person = Backbone.Model.extend({
  defaults: {
    name: '',
    age: 0
  }
});
```
3. Create a collection to store the model instances.
```
var People = Backbone.Collection.extend({
  model: Person
});
```
4. Create a view to render the model and handle user input.
```
var PeopleView = Backbone.View.extend({
  tagName: 'ul',
  render: function(){
    this.collection.each(function(person){
      var personView = new PersonView({ model: person });
      this.$el.append(personView.render().el);
    }, this);
    return this;
  }
});
```
5. Instantiate the model, collection and view.
```
var person = new Person({ name: 'John Doe', age: 30 });
var people = new People([person]);
var peopleView = new PeopleView({ collection: people });
```
6. Render the view.
```
$('#container').html(peopleView.render().el);
```
7. Output:
```
<div id="container">
  <ul>
    <li>John Doe, 30</li>
  </ul>
</div>
```

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/)
- [Getting Started with Backbone.js](https://scotch.io/tutorials/getting-started-with-backbone-js-and-rails-4)

onelinerhub: [How do I create a sample application using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a-sample-application-using-backbone-js)