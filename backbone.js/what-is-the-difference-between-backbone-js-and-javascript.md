# What is the difference between Backbone.js and JavaScript?
// plain

Backbone.js is a JavaScript library that is used to structure web applications. It provides models with key-value binding and custom events, collections with a rich API of enumerable functions, views with declarative event handling, and connects it all to your existing API over a RESTful JSON interface.

JavaScript is a scripting language used to make webpages interactive. It is the language that is used to create the logic of the application and is the main language used to create the functionality of webpages.

The main difference between Backbone.js and JavaScript is that Backbone.js provides structure to the application, while JavaScript provides the logic and functionality.

For example, the following code creates a model in Backbone.js:

```
var Todo = Backbone.Model.extend({
  defaults: {
    title: '',
    completed: false
  }
});

var myTodo = new Todo({
  title: 'Check attributes of the logged user'
});

console.log(myTodo.get('title')); // 'Check attributes of the logged user'
```

## Output example

```
Check attributes of the logged user
```

The code creates a model called Todo with two attributes, title and completed. The model is then instantiated with the title “Check attributes of the logged user”. The get() method is used to retrieve the title of the model which is then logged to the console.

In contrast, the following code is written in JavaScript and is used to create a function that returns the sum of two numbers:

```
function add(x, y) {
  return x + y;
}

console.log(add(1, 2));
```

## Output example

```
3
```

The code creates a function called add which takes two arguments, x and y, and returns the sum of the two numbers. The function is then called with the arguments 1 and 2, and the result is logged to the console.

Overall, Backbone.js is used to structure web applications, while JavaScript is used to create the logic and functionality of the application.

## Helpful links

- Backbone.js: https://backbonejs.org/
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript

onelinerhub: [What is the difference between Backbone.js and JavaScript?](https://onelinerhub.com/backbone.js/what-is-the-difference-between-backbone-js-and-javascript)