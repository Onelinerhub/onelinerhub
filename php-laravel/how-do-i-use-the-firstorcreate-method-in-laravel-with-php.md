# How do I use the firstOrCreate method in Laravel with PHP?
// plain

The `firstOrCreate` method in Laravel with PHP is used to retrieve the first record matching the given criteria, or create a new record if no matching record is found. It is a combination of the `first` and `create` methods.

## Example code

```
$user = App\User::firstOrCreate(
    ['email' => 'john@example.com'],
    ['name' => 'John Doe']
);
```

In the above example, if a user with the email address `john@example.com` already exists in the database, it will be returned. Otherwise, a new user record will be created with the given email address and name.

## Code explanation


1. `App\User`: This is the model class that contains the user records.
2. `firstOrCreate`: This is the method used to retrieve or create a record.
3. `['email' => 'john@example.com']`: This is an array of key-value pairs used to specify the criteria for retrieving an existing record.
4. `['name' => 'John Doe']`: This is an array of key-value pairs used to specify the values of the new record if one is to be created.

## Helpful links

- [Laravel Eloquent: Retrieving Models](https://laravel.com/docs/7.x/eloquent#retrieving-models)
- [Laravel Eloquent: Creating & Updating Models](https://laravel.com/docs/7.x/eloquent#creating-and-updating-models)

onelinerhub: [How do I use the firstOrCreate method in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-firstorcreate-method-in-laravel-with-php)