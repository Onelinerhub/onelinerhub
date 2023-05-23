# How to integrate React with Symfony using PHP?
// plain

Integrating React with Symfony using PHP is a straightforward process. First, install the Symfony Encore Bundle, which provides a bridge between Symfony and React. Then, create a React component and render it in a Symfony template.

```php
// src/Controller/MyController.php

public function index()
{
    return $this->render('my_template.html.twig', [
        'react_component' => React::renderComponent('MyComponent', [
            'name' => 'John Doe',
        ]),
    ]);
}
```

```html
<!-- templates/my_template.html.twig -->

<div id="react-component">
    {{ react_component|raw }}
</div>
```

The code above will render the React component `MyComponent` with the prop `name` set to `John Doe` in the `div` with the `id` of `react-component`.

Parts of the code:

- `React::renderComponent()`: This is a helper method provided by the Symfony Encore Bundle that renders a React component.
- `MyComponent`: This is the name of the React component that will be rendered.
- `name`: This is the prop that will be passed to the React component.

## Helpful links

- [Symfony Encore Bundle](https://symfony.com/doc/current/frontend/encore/installation.html)
- [React Documentation](https://reactjs.org/docs/getting-started.html)

onelinerhub: [How to integrate React with Symfony using PHP?](https://onelinerhub.com/php-symfony/how-to-integrate-react-with-symfony-using-php)