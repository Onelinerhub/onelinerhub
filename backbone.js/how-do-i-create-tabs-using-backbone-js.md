# How do I create tabs using Backbone.js?
// plain

Backbone.js provides a basic structure for creating tabs with the help of the View and Router classes. The View class is responsible for rendering the HTML for each tab, while the Router class is used to handle the navigation between tabs.

To create tabs using Backbone.js, we need to first create a View class for each tab. This View class should have a render method which will return the HTML for the tab. We also need to create a Router class which will handle navigation between the tabs. The Router class should have a `route` method which will take the name of the tab as an argument and will render the corresponding View.

## Example code

```javascript
// View class for tab1
var Tab1View = Backbone.View.extend({
    render: function(){
        return '<div>Tab1 Content</div>';
    }
});

// View class for tab2
var Tab2View = Backbone.View.extend({
    render: function(){
        return '<div>Tab2 Content</div>';
    }
});

// Router class
var TabsRouter = Backbone.Router.extend({
    routes: {
        'tab1': 'showTab1',
        'tab2': 'showTab2'
    },
    showTab1: function(){
        this.renderView(new Tab1View());
    },
    showTab2: function(){
        this.renderView(new Tab2View());
    },
    renderView: function(view){
        $('#container').html(view.render());
    }
});

// Create instance of the router
var router = new TabsRouter();

// Start the router
Backbone.history.start();
```

The code above will create two tabs, `tab1` and `tab2`, and will render the corresponding View when each tab is clicked.

## Code explanation

- `Tab1View` and `Tab2View`: Two View classes for each tab. The `render` method of each View class will return the HTML for the tab.
- `TabsRouter`: Router class with `route` methods for each tab. The `route` methods will render the corresponding View when the tab is clicked.
- `router`: Instance of the Router class.
- `Backbone.history.start()`: This will start the router and enable navigation between tabs.

## Helpful links
- [Backbone.js Documentation](http://backbonejs.org/)
- [Creating Tabs with Backbone.js](https://www.sitepoint.com/creating-tabs-using-backbone-js/)

onelinerhub: [How do I create tabs using Backbone.js?](https://onelinerhub.com/backbone.js/how-do-i-create-tabs-using-backbone-js)