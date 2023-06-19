# How do I install Backbone.js?
// plain

1. Backbone.js can be installed using [npm](https://www.npmjs.com/package/backbone). To install it, open a terminal and type in the following command:

```
npm install backbone
```

2. Alternatively, you can download the [backbone.js source code](https://github.com/jashkenas/backbone/zipball/master) and include it in your project.

3. You can also use a CDN such as [CDNJS](https://cdnjs.com/libraries/backbone.js) to include Backbone.js in your project. To do this, add the following code to the `<head>` of your HTML file:

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.3.3/backbone-min.js"></script>
```

4. You can also use [Bower](https://bower.io/) to install Backbone.js. To do this, open a terminal and type in the following command:

```
bower install backbone
```

5. Once installed, you can start using Backbone.js in your project. For example, you can create a new model using the following code:

```javascript
var MyModel = Backbone.Model.extend({
    defaults: {
        name: '',
        age: 0
    }
});
```

6. You can then create a new instance of the `MyModel` model using the following code:

```javascript
var myModel = new MyModel({
    name: 'John',
    age: 25
});
```

7. You can then access the model's attributes using the `get()` method, like so:

```javascript
myModel.get('name'); // John
myModel.get('age'); // 25
```

For more information on installing and using Backbone.js, please refer to the [official documentation](http://backbonejs.org/).

onelinerhub: [How do I install Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-install-backbone-js)