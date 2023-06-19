# How do I use Backbone.js to create a wiki?
// plain

Backbone.js is a JavaScript library that can be used to create a wiki. To do so, you will need to create a Model, View, and Collection.

The Model will contain the data for each page and will be responsible for validating and persisting the data.

The View will be responsible for rendering the page and responding to user events.

The Collection will contain the list of pages and will be responsible for loading and saving the pages.

## Example code

```
// Model
var Page = Backbone.Model.extend({
    defaults: {
        title: '',
        content: ''
    }
});

// View
var PageView = Backbone.View.extend({
    render: function(){
        this.$el.html(this.model.get('content'));
    }
});

// Collection
var Pages = Backbone.Collection.extend({
    model: Page
});

```

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/)
- [Creating a Wiki with Backbone.js Tutorial](https://www.tutorialspoint.com/backbonejs/backbonejs_wiki_application.htm)

onelinerhub: [How do I use Backbone.js to create a wiki?](https://onelinerhub.com/backbone.js/how-do-i-use-backbone-js-to-create-a-wiki)