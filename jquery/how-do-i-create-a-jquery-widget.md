# How do I create a jQuery widget?
// plain

Creating a jQuery widget is a great way to extend the functionality of jQuery. To create a jQuery widget, you will need to use the jQuery.widget() function. This function takes two parameters, the first being the namespace of the widget, and the second being an object containing the widget's properties and methods.

For example, the following code creates a widget called "MyWidget" with a single method called "init":

```
$.widget("myNamespace.MyWidget", {
    init: function() {
        console.log("MyWidget initialized!");
    }
});
```

The output of this code will be "MyWidget initialized!" in the browser's console.

The object passed into the jQuery.widget() function can contain the following properties and methods:

* **_create()** - This is the method that is called when the widget is first initialized.
* **_init()** - This is the method that is called when the widget is initialized.
* **_setOptions()** - This method is called when the widget's options are set.
* **_destroy()** - This method is called when the widget is destroyed.
* **options** - This is an object containing the widget's options.

For more information about creating jQuery widgets, visit the [jQuery UI Widget Factory Documentation](http://api.jqueryui.com/jQuery.widget/).

onelinerhub: [How do I create a jQuery widget?](https://onelinerhub.com/jquery/how-do-i-create-a-jquery-widget)