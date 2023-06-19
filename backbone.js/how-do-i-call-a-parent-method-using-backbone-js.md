# How do I call a parent method using Backbone.js?
// plain

Backbone.js provides a way to call a parent method using the `__super__` property. `__super__` is a reference to the parent object and can be used to access its methods.

For example, if we have a parent class with a `sayHello()` method and a child class that extends the parent class, we can call the `sayHello()` method from the child class using `__super__` like this:

```
class Parent {
  sayHello() {
    console.log('Hello from the parent class');
  }
}

class Child extends Parent {
  sayHello() {
    // Call the parent method
    this.__super__.sayHello();
    console.log('Hello from the child class');
  }
}

const child = new Child();
child.sayHello();
```

The output of the code above would be:

```
Hello from the parent class
Hello from the child class
```

The `__super__` property can also be used to access the parent object's attributes.

## Code explanation


1. `class Parent { ... }` - This is the parent class that contains the `sayHello()` method.
2. `class Child extends Parent { ... }` - This is the child class that extends the parent class.
3. `this.__super__.sayHello();` - This is how we call the parent's `sayHello()` method from the child class.
4. `const child = new Child();` - This is how we create an instance of the child class.
5. `child.sayHello();` - This is how we call the `sayHello()` method on the child instance.

Here are some ## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/#View-extend)
- [MDN Web Docs - Object.__super__](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/__super__)

onelinerhub: [How do I call a parent method using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-call-a-parent-method-using-backbone-js)