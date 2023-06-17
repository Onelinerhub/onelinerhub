# How can I use jQuery with Webpack?
// plain

jQuery can be used with Webpack by using the npm package manager to install the jQuery library. To install the jQuery library, use the following command:

```
npm install jquery --save
```

Once the jQuery library is installed, you can import it into your Webpack project by adding the following line to your entry point file:

```
import $ from 'jquery';
```

You can then use jQuery in your project by referencing the $ object. For example, you can use jQuery to create a new element and append it to the DOM like this:

```
let newElement = $('<div>My new element</div>');
$('body').append(newElement);
```

You can also use jQuery to make AJAX requests and manipulate the DOM. For example, you can use the following code to make an AJAX request and then update the DOM with the response:

```
$.get('/api/data', function(data) {
  $('#my-element').text(data);
});
```

To learn more about using jQuery with Webpack, you can check out the following links:

- [Webpack and jQuery](https://webpack.js.org/guides/dependency-management/#jquery)
- [Using jQuery with Webpack](https://www.sitepoint.com/using-jquery-with-webpack/)

onelinerhub: [How can I use jQuery with Webpack?](https://onelinerhub.com/jquery/how-can-i-use-jquery-with-webpack)