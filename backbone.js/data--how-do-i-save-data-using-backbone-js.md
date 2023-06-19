# data

How do I save data using Backbone JS?
// plain

Backbone JS provides a way to save data using the `sync` method. This method makes an AJAX request to the server, which can be used to save data.

The following example code shows how to save data using the `sync` method:
```
var MyModel = Backbone.Model.extend({
  urlRoot: '/mymodel'
});

var myModel = new MyModel({name: 'My Model'});
myModel.save();
```
This code will send an AJAX request to the server with the data `{name: 'My Model'}`.

The `sync` method also takes a `success` callback, which will be called when the AJAX request is successful:
```
myModel.save({}, {
  success: function() {
    console.log('Data saved successfully!');
  }
});
```
This code will print 'Data saved successfully!' to the console when the AJAX request is successful.

The `sync` method also takes an `error` callback, which will be called when the AJAX request fails:
```
myModel.save({}, {
  error: function() {
    console.log('Error saving data!');
  }
});
```
This code will print 'Error saving data!' to the console when the AJAX request fails.

The `sync` method can also be used to fetch data from the server:
```
myModel.fetch({
  success: function() {
    console.log('Data fetched successfully!');
  }
});
```
This code will print 'Data fetched successfully!' to the console when the AJAX request is successful.

## Helpful links
* http://backbonejs.org/#Sync
* http://backbonejs.org/#Model-fetch

onelinerhub: [data

How do I save data using Backbone JS?](https://onelinerhub.com/backbone.js/data--how-do-i-save-data-using-backbone-js)