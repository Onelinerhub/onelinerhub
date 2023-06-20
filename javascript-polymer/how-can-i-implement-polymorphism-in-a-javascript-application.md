# How can I implement polymorphism in a JavaScript application?
// plain

Polymorphism in JavaScript can be implemented using the `prototype` object. Polymorphism allows the same interface to be used to access different objects. To illustrate this concept, consider the following example:

```js
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function() {
  console.log(`${this.name} says something`);
}

function Cat(name) {
  Animal.call(this, name);
}

Cat.prototype = Object.create(Animal.prototype);

Cat.prototype.speak = function() {
  console.log(`${this.name} meows`);
}

const animal = new Animal('Animal');
const cat = new Cat('Cat');

animal.speak(); // Animal says something
cat.speak(); // Cat meows
```

In the example, `Animal` and `Cat` are two different objects. However, both objects have a `speak` method which is defined in the `prototype` object. This allows the same interface to be used to access different objects.

## Code explanation

1. `function Animal(name)` - This is the constructor function for the Animal object. It takes a name as an argument and sets it as a property of the object.
2. `Animal.prototype.speak` - This is a method of the Animal object which is defined in the prototype object. It logs a message to the console.
3. `function Cat(name)` - This is the constructor function for the Cat object. It takes a name as an argument and sets it as a property of the object.
4. `Cat.prototype = Object.create(Animal.prototype)` - This line sets the prototype of the Cat object to the prototype of the Animal object. This allows the same interface to be used for both objects.
5. `Cat.prototype.speak` - This is a method of the Cat object which is defined in the prototype object. It logs a message to the console.

## Helpful links
- [MDN - Object.create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)
- [MDN - Prototypes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/prototype)

onelinerhub: [How can I implement polymorphism in a JavaScript application?](https://onelinerhub.com/javascript-polymer/how-can-i-implement-polymorphism-in-a-javascript-application)