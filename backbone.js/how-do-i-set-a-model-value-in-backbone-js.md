# How do I set a model value in Backbone.js?
// plain

Backbone.js provides a set() method to set model values. The set() method takes two arguments, the first argument is the attribute name and the second argument is the value. The set() method will set the attribute on the model and fire a "change" event.

## Example

```
var model = new Backbone.Model({
  name: 'John Doe'
});

model.set('name', 'Jane Doe');

console.log(model.get('name'));
```
## Output example

```
Jane Doe
```

The set() method can also take an object as an argument, in which case it will set multiple attributes on the model.

## Example

```
var model = new Backbone.Model({
  name: 'John Doe',
  age: 25
});

model.set({
  name: 'Jane Doe',
  age: 30
});

console.log(model.get('name'));
console.log(model.get('age'));
```
## Output example

```
Jane Doe
30
```

The set() method can also take an option as the third argument. The "silent" option will prevent the "change" event from being fired.

## Example

```
var model = new Backbone.Model({
  name: 'John Doe'
});

model.on('change', function() {
  console.log('model changed');
});

model.set('name', 'Jane Doe', { silent: true });
```
## Output example


None

onelinerhub: [How do I set a model value in Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-set-a-model-value-in-backbone-js)