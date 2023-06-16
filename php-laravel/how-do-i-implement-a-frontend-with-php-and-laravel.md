# How do I implement a frontend with PHP and Laravel?
// plain

To implement a frontend with PHP and Laravel, you can use the Blade templating engine. Blade is a simple, yet powerful templating engine provided with Laravel. It allows you to use plain PHP code in your views.

For example, the following code block will display "Hello World" in the browser:
```
<h1>Hello World</h1>
```

## Output example

```
Hello World
```

Blade also provides a convenient way to pass data from the controller to the view. For example, the following code block will display the value of the $name variable:

```
<h1>Hello {{ $name }}</h1>
```

## Output example

```
Hello John
```

## Code explanation

- `<h1>Hello World</h1>`: This is a HTML tag used to display "Hello World" in the browser.
- `<h1>Hello {{ $name }}</h1>`: This is a Blade tag used to display the value of the $name variable in the browser.

## Helpful links
- [Laravel Blade Documentation](https://laravel.com/docs/7.x/blade)
- [Laravel Passing Data To Views](https://laravel.com/docs/7.x/views#passing-data-to-views)

onelinerhub: [How do I implement a frontend with PHP and Laravel?](https://onelinerhub.com/php-laravel/how-do-i-implement-a-frontend-with-php-and-laravel)