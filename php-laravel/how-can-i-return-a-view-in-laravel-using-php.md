# How can I return a view in Laravel using PHP?
// plain

To return a view in Laravel using PHP, you can use the `view()` helper function. This function accepts two parameters: a view name and an array of data that should be passed to the view.

For example:

```
$data = [
    'name' => 'John'
];

return view('welcome', $data);
```

This will return the `welcome` view with the `$data` array available for use in the view.

## Code explanation


- `$data`: an array of data that should be passed to the view.
- `view()`: the `view()` helper function that accepts two parameters: a view name and an array of data.
- `return view('welcome', $data);`: this will return the `welcome` view with the `$data` array available for use in the view.

## Helpful links

- [Laravel - Views](https://laravel.com/docs/7.x/views)
- [Laravel - Blade Templates](https://laravel.com/docs/7.x/blade)

onelinerhub: [How can I return a view in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-can-i-return-a-view-in-laravel-using-php)