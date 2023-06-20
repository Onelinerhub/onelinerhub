# How can I use Vue.js to create a Model-View-Controller (MVC) architecture?
// plain

Vue.js is an open-source JavaScript framework that can be used to create a Model-View-Controller (MVC) architecture. This architecture allows developers to separate the application logic, data, and user interface.

A basic MVC architecture in Vue.js consists of three parts - the Model, View, and Controller. The Model is the data layer that stores the application data. The View is the user interface layer that displays the data. The Controller is the logic layer that handles the user interaction and updates the Model and View.

Below is an example of how to create a basic MVC architecture in Vue.js:

```
// Create the Model
var data = {
  message: 'Hello World!'
};

// Create the View
var app = new Vue({
  el: '#app',
  data: data
});

// Create the Controller
function updateMessage() {
  data.message = 'Goodbye World!';
}
```

The output of this code is a webpage with the message "Hello World!" which can be updated when the updateMessage() function is called.

Parts of the code:

1. The Model is the data layer that stores the application data. In this example, the Model is the `data` variable which stores the `message` property.
2. The View is the user interface layer that displays the data. In this example, the View is the `app` variable which is a Vue instance that binds the `data` variable to the DOM element with the `id` of `app`.
3. The Controller is the logic layer that handles the user interaction and updates the Model and View. In this example, the Controller is the `updateMessage()` function which updates the `message` property in the `data` variable.

## Helpful links

- [Vue.js Documentation](https://vuejs.org/v2/guide/)
- [Vue.js MVC Example](https://alligator.io/vuejs/mvc-example/)

onelinerhub: [How can I use Vue.js to create a Model-View-Controller (MVC) architecture?](https://onelinerhub.com/vue.js/how-can-i-use-vue-js-to-create-a-model-view-controller--mvc--architecture)