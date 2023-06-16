# How do I use Laravel validation in PHP?
// plain

Laravel validation is an easy way to validate user input in a Laravel application. It can be used in PHP to validate user input in forms.

The basic syntax of Laravel validation is:

```
$validator = Validator::make($data, $rules);
```

where `$data` is an array of data to be validated and `$rules` is an array of validation rules.

For example, to validate a user's email address:

```
$data = array('email' => 'example@example.com');
$rules = array('email' => 'required|email');
$validator = Validator::make($data, $rules);
```

The output of this code will be a boolean (`true` or `false`) depending on whether the validation was successful or not.

In addition, you can also add custom error messages to the validation rules like this:

```
$rules = array('email' => 'required|email|unique:users,email');
$messages = array('unique' => 'This email address is already in use.');
$validator = Validator::make($data, $rules, $messages);
```

The output of this code will be the custom error message if the validation fails.

For more information, see the [Laravel documentation](https://laravel.com/docs/7.x/validation) and the [Laravel Validation Tutorial](https://laraveldaily.com/laravel-validation-tutorial/).

onelinerhub: [How do I use Laravel validation in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-validation-in-php)