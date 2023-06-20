# How do I create a Polymer JavaScript app?
// plain

To create a Polymer JavaScript app, you need to first install the Polymer CLI. This can be done with the command `npm install -g polymer-cli`.

Then, you can create a new project with `polymer init` and choose the `polymer-3-application` template. This will create a basic Polymer 3 app structure with the following files:

* `index.html`: This is the main entry point for the application.
* `manifest.json`: This contains metadata about the application.
* `src/my-app.js`: This contains the main application logic.
* `src/my-view1.js`: This contains the logic for the first view.
* `src/my-view2.js`: This contains the logic for the second view.
* `src/shared-styles.js`: This contains shared styles for all the views.

You can then add your own custom elements and logic to create the app you want.

## Example code

```
<dom-module id="my-app">
  <template>
    <style include="shared-styles">
      :host {
        display: block;
      }
    </style>

    <h1>Hello [[name]]</h1>
  </template>

  <script>
    class MyApp extends Polymer.Element {
      static get is() { return 'my-app'; }
      static get properties() {
        return {
          name: {
            type: String,
            value: 'World'
          }
        }
      }
    }
    customElements.define(MyApp.is, MyApp);
  </script>
</dom-module>
```

## Output example

`Hello World`

## Helpful links
* [Polymer CLI](https://www.polymer-project.org/3.0/docs/tools/polymer-cli)
* [Polymer 3 App Structure](https://www.polymer-project.org/3.0/docs/start/reusable-elements)

onelinerhub: [How do I create a Polymer JavaScript app?](https://onelinerhub.com/javascript-polymer/how-do-i-create-a-polymer-javascript-app)