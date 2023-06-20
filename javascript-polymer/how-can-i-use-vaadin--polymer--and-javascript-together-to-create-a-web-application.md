# How can I use Vaadin, Polymer, and JavaScript together to create a web application?
// plain

Vaadin, Polymer, and JavaScript can be used together to create a web application. Vaadin is a Java-based web framework that allows developers to create web applications using Java and HTML. Polymer is a JavaScript library that allows developers to create custom HTML elements. JavaScript is a scripting language that can be used to create interactive web applications.

The following example code shows how to use Vaadin, Polymer, and JavaScript together to create a web application.

```
<div id="app">
  <vaadin-button on-click="myFunction()">Click Me</vaadin-button>
</div>

<script>
  function myFunction() {
    // create custom element using Polymer
    var myElement = document.createElement('my-element');

    // add custom element to the DOM
    document.getElementById('app').appendChild(myElement);
  }
</script>
```

In this example, a Vaadin button is created and when clicked, a custom element is created using Polymer and added to the DOM using JavaScript.

## Code explanation


- `<div id="app">` - creates a `div` element with an `id` of `app`
- `<vaadin-button on-click="myFunction()">Click Me</Vaadin-button>` - creates a Vaadin button with an `on-click` event handler that calls the `myFunction()` function
- `function myFunction()` - creates a function named `myFunction()`
- `var myElement = document.createElement('my-element');` - creates a custom element using Polymer
- `document.getElementById('app').appendChild(myElement);` - adds the custom element to the DOM

## Helpful links

- [Vaadin](https://vaadin.com/)
- [Polymer](https://www.polymer-project.org/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

onelinerhub: [How can I use Vaadin, Polymer, and JavaScript together to create a web application?](https://onelinerhub.com/javascript-polymer/how-can-i-use-vaadin--polymer--and-javascript-together-to-create-a-web-application)