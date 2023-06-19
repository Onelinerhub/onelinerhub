# cript

How can I use Backbone with Bonescript?
// plain

Backbone.js is a client-side JavaScript library that can be used with Bonescript to create dynamic web applications. Bonescript is a JavaScript library for the BeagleBone platform which provides an API for controlling GPIO pins, I2C, SPI, UARTs, analog inputs, and other features.

Using Backbone with Bonescript is a great way to create interactive web applications that can control the BeagleBone's hardware.

Example code to get started:

```
// Set up Bonescript
var b = require('bonescript');

// Set up Backbone
var Backbone = require('backbone');

// Create a model
var MyModel = Backbone.Model.extend({
    // Set default values
    defaults: {
        pin: 'P8_13',
        state: 0
    },
    // Toggle the state
    toggle: function() {
        this.set('state', this.get('state') ? 0 : 1);
    }
});

// Create an instance of the model
var myModel = new MyModel();

// Listen for changes to the model
myModel.on('change', function() {
    // Set the pin state
    b.digitalWrite(myModel.get('pin'), myModel.get('state'));
});

// Toggle the state
myModel.toggle();
```

This code creates a Backbone model with a `toggle` function which sets the state to either 0 or 1. It then listens for changes to the model and uses Bonescript to set the pin state accordingly.

The code consists of the following parts:

- `require('bonescript')`: Loads the Bonescript library.
- `require('backbone')`: Loads the Backbone library.
- `Backbone.Model.extend()`: Creates a Backbone Model with default values.
- `myModel.on('change', function() {})`: Listens for changes to the model.
- `b.digitalWrite(myModel.get('pin'), myModel.get('state'))`: Sets the pin state with Bonescript.
- `myModel.toggle()`: Toggles the state of the model.

## Helpful links

- [Backbone.js](http://backbonejs.org/)
- [Bonescript](https://github.com/jadonk/bonescript)

onelinerhub: [cript

How can I use Backbone with Bonescript?](https://onelinerhub.com/backbone.js/cript--how-can-i-use-backbone-with-bonescript)