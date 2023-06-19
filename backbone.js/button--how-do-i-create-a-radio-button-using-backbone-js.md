# button

How do I create a radio button using Backbone.js?
// plain

Radio buttons are a type of HTML input element that allows a user to select one option from a list of options. In Backbone.js, radio buttons can be created using the `input` view. The `input` view takes a `type` option which should be set to `'radio'` to create a radio button.

The following example creates a radio button with the id `myRadio` and the label `My Radio`:

```javascript
var RadioButton = Backbone.View.extend({
  tagName: 'input',
  attributes: {
    type: 'radio',
    id: 'myRadio'
  },
  events: {
    'click': 'onClick'
  },
  onClick: function(e) {
    // Handle click event
  },
  render: function() {
    this.$el.attr('checked', this.model.get('checked'));
    return this;
  }
});

var myRadioButton = new RadioButton({
  model: new Backbone.Model({
    label: 'My Radio',
    checked: false
  })
});

$('body').append(myRadioButton.render().el);
```

This code will render an HTML element like this:

```html
<input type="radio" id="myRadio" checked="false">
```

The code consists of the following parts:

- `RadioButton`: The view which extends `Backbone.View` and sets the `tagName` to `input` and the `type` attribute to `radio`. It also sets the `id` to `myRadio` and adds an event handler for the `click` event.
- `myRadioButton`: The instance of the `RadioButton` view. It is passed a model with the label `My Radio` and a `checked` attribute set to `false`.
- `render()`: The render function which sets the `checked` attribute of the `el` to the value of the model's `checked` attribute.

For more information, see the [Backbone.js docs on views](http://backbonejs.org/#View) and the [MDN docs on radio buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio).

onelinerhub: [button

How do I create a radio button using Backbone.js?](https://onelinerhub.com/backbone.js/button--how-do-i-create-a-radio-button-using-backbone-js)