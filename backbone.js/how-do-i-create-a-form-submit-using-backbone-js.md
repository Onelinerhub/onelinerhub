# How do I create a form submit using Backbone.js?
// plain

Backbone.js provides a simple way to create a form submit. To do this, you will need to create a model, a view, and a template.

First, create a model with the attributes you want to submit in the form. For example:

```
var FormModel = Backbone.Model.extend({
    defaults: {
        name: '',
        email: ''
    }
});
```

Next, create a view that will contain the template, and handle the form submit. The view should bind to the model, and listen for the submit event. For example:

```
var FormView = Backbone.View.extend({
    el: '#form',
    model: new FormModel(),
    template: _.template($('#form-template').html()),
    events: {
        'submit': 'handleSubmit'
    },
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    },
    handleSubmit: function(e) {
        e.preventDefault();
        //handle the form submit here
    }
});
```

Finally, create a template to render the form. It should contain the form elements and the submit button. For example:

```
<script type="text/template" id="form-template">
    <form>
        <input type="text" name="name" value="<%= name %>" />
        <input type="text" name="email" value="<%= email %>" />
        <input type="submit" value="Submit" />
    </form>
</script>
```

Now you can create a new instance of the view and render it:

```
var formView = new FormView();
formView.render();
```

The form submit will now be handled by the `handleSubmit` function in the view.

## Helpful links

- [Backbone.js Documentation](http://backbonejs.org/)
- [Backbone.js Models](http://backbonejs.org/#Model)
- [Backbone.js Views](http://backbonejs.org/#View)
- [Backbone.js Templates](http://backbonejs.org/#View-templates)

onelinerhub: [How do I create a form submit using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-a-form-submit-using-backbone-js)