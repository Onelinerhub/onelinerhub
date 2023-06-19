# How do I create a modal dialog using Backbone.js?
// plain

Creating a modal dialog using Backbone.js is relatively easy. The following example code will create a modal dialog:

```
// Create a new Backbone view
var ModalDialog = Backbone.View.extend({
  // Set the template
  template: _.template("<div class='modal-dialog'> <div> <h1><%= title %></h1> <p><%= message %></p> </div> </div>"),
  // Initialize the view
  initialize: function(options) {
    this.title = options.title;
    this.message = options.message;
  },
  // Render the view
  render: function() {
    var html = this.template({
      title: this.title,
      message: this.message
    });
    this.$el.html(html);
    return this;
  }
});

// Create a new instance of the modal dialog
var modal = new ModalDialog({
  title: 'My Modal Dialog',
  message: 'This is my modal dialog!'
});

// Render the modal dialog
modal.render();
```

The rendered modal dialog will look like this:

```
<div class="modal-dialog">
  <div>
    <h1>My Modal Dialog</h1>
    <p>This is my modal dialog!</p>
  </div>
</div>
```

## Code explanation


* `ModalDialog` - This is the Backbone view object that contains the template and logic for the modal dialog.
* `template` - The template is a _.template() function that contains the HTML for the modal dialog.
* `initialize` - This is the function that is called when the view is initialized and sets the title and message options.
* `render` - This is the function that is called to render the view and creates the HTML for the modal dialog.

## Helpful links

* [Backbone.js](http://backbonejs.org/)
* [Underscore.js](http://underscorejs.org/)
* [Backbone.View](http://backbonejs.org/#View)

onelinerhub: [How do I create a modal dialog using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a-modal-dialog-using-backbone-js)