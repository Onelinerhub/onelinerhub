# How do I use Lodash templates with JavaScript?
// plain

Lodash templates are a powerful way to use JavaScript to create dynamic HTML content. They use a syntax similar to the popular Underscore.js library, but with additional features.

To use Lodash templates with JavaScript, you first need to include the Lodash library in your project. You can do this by downloading the library from the [Lodash website](https://lodash.com/).

Once the library is included, you can create a Lodash template by defining a string with the template syntax. For example:

```
let template = `
  <div>
    <h1>Hello, <%= name %></h1>
  </div>
`;
```

The template syntax consists of HTML tags combined with placeholders for dynamic content. In this example, the placeholder `<%= name %>` will be replaced with a value when the template is used.

To use the template, you can call the `_.template()` function from Lodash, passing it the template string. This will return a function that can be used to generate the HTML output.

```
let outputFn = _.template(template);
let outputHtml = outputFn({ name: 'John' });

console.log(outputHtml);
```

## Output example

```
<div>
  <h1>Hello, John</h1>
</div>
```

Lodash templates can be used to generate HTML for any type of content, and can be combined with other JavaScript code to create dynamic web pages.

onelinerhub: [How do I use Lodash templates with JavaScript?](https://onelinerhub.com/javascript-lodash/how-do-i-use-lodash-templates-with-javascript)