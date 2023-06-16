# validation

How do I implement input validation in a Laravel application using PHP?
// plain

Validation in Laravel is simple and easy to implement. Here is an example of how to validate a form input using Laravel's Validator class:

```php
$data = request()->validate([
    'name' => 'required|max:255',
    'email' => 'required|email',
    'password' => 'required|confirmed',
]);
```

This code will validate the `name`, `email` and `password` fields of the form. The `required` rule means that the field is required and must be filled in, while the `max` rule will ensure that the name field does not exceed 255 characters. The `email` rule will validate the email address, and the `confirmed` rule will ensure that the password is confirmed by the user.

The above code will return an array of validated data if the validation passes, otherwise it will throw an exception.

The following list explains the parts of the code above:

- `request()`: This is a method of the Request class which is used to retrieve the request data.
- `validate()`: This is a method of the Request class which is used to validate the request data.
- `required`: This is a validation rule which ensures that the field is filled in.
- `max`: This is a validation rule which ensures that the field does not exceed a certain length.
- `email`: This is a validation rule which ensures that the field is a valid email address.
- `confirmed`: This is a validation rule which ensures that the field is confirmed by the user.

Here are some relevant links for more information:

- [Laravel Documentation - Validation](https://laravel.com/docs/7.x/validation)
- [Laravel API - Request](https://laravel.com/api/7.x/Illuminate/Http/Request.html)

onelinerhub: [validation

How do I implement input validation in a Laravel application using PHP?](https://onelinerhub.com/php-laravel/validation--how-do-i-implement-input-validation-in-a-laravel-application-using-php)