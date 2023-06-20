# How can I use JavaScript and Polymer together to create a web application?
// plain

JavaScript and Polymer can be used together to create a web application. Polymer is a JavaScript library that allows developers to create custom HTML elements and use them in their web applications. By combining JavaScript and Polymer, developers can create interactive and dynamic web applications that are easy to maintain.

For example, the following code creates a custom element called `<my-element>`. The `<my-element>` element contains a button that, when clicked, prints a message to the console.

```javascript
<script>
    class MyElement extends Polymer.Element {
        static get is() { return 'my-element'; }
        constructor() {
            super();
        }
        ready() {
            super.ready();
            this.$.myButton.addEventListener('click', () => {
                console.log('Button clicked!');
            });
        }
    }
    customElements.define(MyElement.is, MyElement);
</script>

<my-element>
    <button id="myButton">Click me</button>
</my-element>
```

When the button is clicked, the following output is printed to the console:

```
Button clicked!
```

This example code demonstrates how simple it is to create a custom element and use it in a web application. By combining JavaScript and Polymer, developers can create powerful and interactive web applications.

## Helpful links
* [Polymer Project](https://www.polymer-project.org/)
* [Custom Elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)

onelinerhub: [How can I use JavaScript and Polymer together to create a web application?](https://onelinerhub.com/javascript-polymer/how-can-i-use-javascript-and-polymer-together-to-create-a-web-application)