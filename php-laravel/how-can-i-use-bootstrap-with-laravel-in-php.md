# How can I use Bootstrap with Laravel in PHP?
// plain

To use Bootstrap with Laravel in PHP, you can include the Bootstrap CSS and JavaScript files into your project. You can do this by adding the following code to your `<head>` tag:

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
```

You can also use Laravel Mix, a wrapper around Webpack, to compile your Sass files into CSS and your JavaScript files into a single file. To do this, first install the laravel-mix package:

```bash
npm install laravel-mix --save-dev
```

Then, create a `webpack.mix.js` file in the root of your project and add the following code:

```js
const mix = require('laravel-mix');

mix.js('resources/js/app.js', 'public/js')
   .sass('resources/sass/app.scss', 'public/css');
```

Finally, run the following command to compile your files:

```bash
npm run dev
```

Parts of Code:

1. `<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">` - This code adds the Bootstrap CSS file into your project.

2. `<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>` - This code adds the Bootstrap JavaScript file into your project.

3. `npm install laravel-mix --save-dev` - This command installs the laravel-mix package, which is a wrapper around Webpack.

4. `const mix = require('laravel-mix');` - This code adds the laravel-mix package into your project.

5. `mix.js('resources/js/app.js', 'public/js')` - This code compiles your JavaScript files into a single file.

6. `mix.sass('resources/sass/app.scss', 'public/css');` - This code compiles your Sass files into CSS.

7. `npm run dev` - This command compiles your files.

## Helpful links

- [Bootstrap](https://getbootstrap.com/)
- [Laravel Mix](https://laravel.com/docs/5.7/mix)
- [Webpack](https://webpack.js.org/)

onelinerhub: [How can I use Bootstrap with Laravel in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-bootstrap-with-laravel-in-php)