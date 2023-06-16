# How can I use React with PHP Laravel?
// plain

React can be used with PHP Laravel by having the React components in the Laravel application. The components can be rendered in the Blade template.

## Example code


```
<div id="app">
    <example-component></example-component>
</div>

<script>
    ReactDOM.render(
        <ExampleComponent />,
        document.getElementById('app')
    );
</script>
```

The React components can be included in the `resources/js/app.js` file. This file is compiled by Laravel Mix.

## Example code


```
import React from 'react';
import ReactDOM from 'react-dom';

import ExampleComponent from './components/ExampleComponent';

ReactDOM.render(
    <ExampleComponent />,
    document.getElementById('app')
);
```

The compiled file can be included in the Blade template.

## Example code


```
<html>
    <head>
        <title>Example</title>
    </head>
    <body>
        <div id="app"></div>

        <script src="{{ mix('js/app.js') }}"></script>
    </body>
</html>
```

This will render the React component in the `#app` element.

## Helpful links

- [React with Laravel](https://laravel-news.com/react-laravel)
- [Integrating React into an Existing Laravel Application](https://laravel.com/docs/5.8/frontend#writing-vue-components)

onelinerhub: [How can I use React with PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-use-react-with-php-laravel)