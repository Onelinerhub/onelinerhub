# How can I use an SVG icon in an Express.js application?
// plain

Using an SVG icon in an Express.js application is fairly simple.

First, you'll need to create a folder for the SVG files and place them in the public directory of your Express.js application.

Then, you can use a template engine such as EJS to render the SVG file in the HTML page.

For example, a basic EJS template for an SVG file would look like this:

```
<img src="<%= icon %>" alt="Icon" />
```

In the Express.js route, you can then pass the SVG file path as a parameter to the template.

```
res.render('index', { icon: '/svg/icon.svg' });
```

The output of this code will be an image tag with the SVG file source.

```
<img src="/svg/icon.svg" alt="Icon" />
```

## Helpful links
- [EJS Templating](https://ejs.co/)
- [Express.js Routing](https://expressjs.com/en/guide/routing.html)

onelinerhub: [How can I use an SVG icon in an Express.js application?](https://onelinerhub.com/expressjs/how-can-i-use-an-svg-icon-in-an-express-js-application)