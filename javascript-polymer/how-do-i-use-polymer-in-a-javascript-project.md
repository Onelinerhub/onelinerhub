# How do I use Polymer in a JavaScript project?
// plain

Using Polymer in a JavaScript project is fairly straightforward.

First, you need to include the Polymer library in your HTML file:
```html
<script src="https://polygit.org/components/webcomponentsjs/webcomponents-lite.js"></script>
```

Next, you need to define your custom element using the `<dom-module>` tag:
```html
<dom-module id="my-element">
  <template>
    <style>
      /* CSS styles go here */
    </style>
    <!-- HTML markup goes here -->
  </template>
  <script>
    // JavaScript code goes here
  </script>
</dom-module>
```

Finally, you need to register your custom element:
```javascript
  Polymer({
    is: 'my-element'
  });
```

Now your custom element is ready to use in your JavaScript project.

Parts of the code explained:

1. `<script src="https://polygit.org/components/webcomponentsjs/webcomponents-lite.js"></script>`: This line of code is used to include the Polymer library in your HTML file.

2. `<dom-module id="my-element">`: This tag is used to define your custom element.

3. `<template>`: This tag is used to define the HTML markup and CSS styles for your custom element.

4. `<script>`: This tag is used to define the JavaScript code for your custom element.

5. `Polymer({ is: 'my-element' });`: This line of code is used to register your custom element.

## Helpful links

1. [Getting Started with Polymer](https://www.polymer-project.org/2.0/start/first-element/intro)
2. [Polymer Documentation](https://www.polymer-project.org/2.0/docs/devguide/feature-overview)

onelinerhub: [How do I use Polymer in a JavaScript project?](https://onelinerhub.com/javascript-polymer/how-do-i-use-polymer-in-a-javascript-project)