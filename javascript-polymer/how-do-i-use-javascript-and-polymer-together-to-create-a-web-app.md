# How do I use Javascript and Polymer together to create a web app?
// plain

Using Javascript and Polymer together to create a web app is a powerful combination. Polymer is a library of web components that can be used to create modern web applications. To use them, you need to include the Polymer library in your HTML file:

```
<script src="https://unpkg.com/@polymer/polymer/polymer-legacy.html"></script>
```

You can then create custom web components using the Polymer library. For example, here is a simple component that displays a greeting:

```
<dom-module id="my-element">
  <template>
    <h2>Hello, <span>{{name}}</span></h2>
  </template>
  <script>
    Polymer({
      is: 'my-element',
      properties: {
        name: String
      }
    });
  </script>
</dom-module>
```

The code above creates a custom element called `my-element` that can be used in the HTML. To use this element, you need to register it with the Polymer library:

```
<script>
  window.addEventListener('WebComponentsReady', function() {
    Polymer({is: 'my-element'});
  });
</script>
```

You can then use the element in the HTML like this:

```
<my-element name="World"></my-element>
```

This would display the greeting `Hello, World` on the page.

You can use Javascript to interact with the elements and manipulate the DOM. For example, if you wanted to change the greeting when a button is clicked, you could do this:

```
<script>
  document.querySelector('my-element').name = 'Foo';
</script>
```

This would change the greeting to `Hello, Foo` when the button is clicked.

Using Javascript and Polymer together, you can create powerful and interactive web apps.

## Code explanation

1. `<script src="https://unpkg.com/@polymer/polymer/polymer-legacy.html"></script>` - This line includes the Polymer library in the HTML file.
2. `<dom-module id="my-element">` - This creates a custom web component called `my-element`.
3. `<template>` - This is the template for the element. It contains the HTML that will be displayed on the page.
4. `<script>` - This is where the Javascript code for the element goes.
5. `Polymer({ is: 'my-element', properties: { name: String } });` - This registers the element with the Polymer library.
6. `window.addEventListener('WebComponentsReady', function() { Polymer({is: 'my-element'}); });` - This registers the element with the Polymer library.
7. `<my-element name="World"></my-element>` - This uses the element in the HTML.
8. `document.querySelector('my-element').name = 'Foo';` - This changes the greeting when a button is clicked.

## Helpful links
- [Polymer Project](https://www.polymer-project.org/)
- [Web Components](https://developer.mozilla.org/en-US/docs/Web/Web_Components)
- [Using Polymer with Javascript](https://www.polymer-project.org/3.0/docs/devguide/feature-overview#using-javascript)

onelinerhub: [How do I use Javascript and Polymer together to create a web app?](https://onelinerhub.com/javascript-polymer/how-do-i-use-javascript-and-polymer-together-to-create-a-web-app)