# How do I organize the structure of a Backbone.js project?
// plain

A Backbone.js project should be organized in the following way:

1. Create a project folder and add the following files:
    - `index.html`
    - `main.js`
    - `style.css`
2. Include the Backbone.js library in the `index.html` file:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.3.3/backbone-min.js"></script>
```
3. Create a `models` folder and add `model.js` file for the application models.
4. Create a `views` folder and add `view.js` file for the application views.
5. Create a `collections` folder and add `collection.js` file for the application collections.
6. Create a `routers` folder and add `router.js` file for the application routers.
7. Include all the necessary files in the `index.html` file:
```html
<script src="models/model.js"></script>
<script src="views/view.js"></script>
<script src="collections/collection.js"></script>
<script src="routers/router.js"></script>
<script src="main.js"></script>
```

This should provide a basic structure for a Backbone.js project.

Additional Resources:
- [Backbone.js Documentation](https://backbonejs.org/#getting-started)
- [Organizing Backbone Projects](https://addyosmani.com/blog/organizing-backbone-projects/)

onelinerhub: [How do I organize the structure of a Backbone.js project?](https://onelinerhub.com/backbone.js/how-do-i-organize-the-structure-of-a-backbone-js-project)