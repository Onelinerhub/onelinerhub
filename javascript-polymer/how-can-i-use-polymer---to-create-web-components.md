# How can I use Polymer 3 to create web components?
// plain

Polymer 3 is a library that allows developers to create custom web components. Web components are reusable pieces of code that can be used across multiple web applications.

To create a web component in Polymer 3, you need to define a class that extends the Polymer.Element base class. Within the class, you can define custom properties and methods, as well as the template for your component.

For example, the following code creates a simple web component that displays a greeting:

```js
class Greeting extends Polymer.Element {
  static get is() { return 'greeting-element'; }
  static get properties() {
    return {
      name: {
        type: String,
        value: 'World'
      }
    };
  }
  constructor() {
    super();
  }
  _render({name}) {
    return html`<h1>Hello, ${name}!</h1>`;
  }
}
customElements.define(Greeting.is, Greeting);
```

The code defines a class called `Greeting` that extends the `Polymer.Element` base class. It defines a custom property called `name` and a method called `_render` which is used to render the HTML template. Finally, the `customElements.define` method is used to register the web component.

The output of this code would be a `<greeting-element>` HTML element that displays a greeting when used in an HTML page.

Links:

- [Polymer 3 Documentation](https://www.polymer-project.org/3.0/docs/devguide/feature-overview)
- [Creating Web Components with Polymer 3](https://www.webcomponents.org/introduction/creating-web-components-with-polymer-3)

onelinerhub: [How can I use Polymer 3 to create web components?](https://onelinerhub.com/javascript-polymer/how-can-i-use-polymer---to-create-web-components)