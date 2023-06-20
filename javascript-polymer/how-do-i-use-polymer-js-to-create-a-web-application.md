# How do I use Polymer JS to create a web application?
// plain

Polymer JS is a JavaScript library that can be used to create web applications. It allows developers to create custom HTML elements and use them in their applications.

To use Polymer JS to create a web application, you need to first create a custom element by using the `<dom-module>` tag. Inside the `<dom-module>`, you can define the element's properties, methods, and events.

For example, the following code creates a custom element called `my-element` with a property called `name`:
```
<dom-module id="my-element">
  <template>
    <p>My name is {{name}}</p>
  </template>
  <script>
    Polymer({
      is: 'my-element',
      properties: {
        name: {
          type: String
        }
      }
    });
  </script>
</dom-module>
```

Once the custom element is created, you can use it in your application. For example, the following HTML code will create an instance of the `my-element` element and set its `name` property to `John`:

```
<my-element name="John"></my-element>
```

## Output example

My name is John

You can also use Polymer JS to create custom elements with data binding. This allows you to bind data from the application to the custom element, so that the element will update whenever the data changes.

To learn more about using Polymer JS to create web applications, you can check out the [Polymer JS documentation](https://www.polymer-project.org/3.0/docs/devguide/feature-overview).

onelinerhub: [How do I use Polymer JS to create a web application?](https://onelinerhub.com/javascript-polymer/how-do-i-use-polymer-js-to-create-a-web-application)