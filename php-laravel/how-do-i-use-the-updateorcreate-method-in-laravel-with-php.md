# How do I use the updateOrCreate method in Laravel with PHP?
// plain

The `updateOrCreate` method in Laravel can be used to update an existing record in the database, or create a new record if none exists. It is commonly used when a user is signing up for a service or creating an account. The syntax is as follows:

```
Model::updateOrCreate(
    ['attribute' => $value],
    ['other_attribute' => $other_value]
);
```

The first parameter is an array of attributes to match, and the second parameter is an array of values to set if a new record is created.

For example, if we have a `User` model with the attributes `email` and `name`, we could use the following code to update an existing user with the email `example@example.com` or create a new user if none exists:

```
$user = User::updateOrCreate(
    ['email' => 'example@example.com'],
    ['name' => 'John Smith']
);
```

The `$user` variable will now contain the user object, either the existing user or the newly created user.

## Code explanation


- `Model::updateOrCreate`: The static method to call on the relevant model.
- `['attribute' => $value]`: An array of attributes to match.
- `['other_attribute' => $other_value]`: An array of values to set if a new record is created.

#### List of relevant links if any:

- [Laravel Documentation - Retrieving & Updating Models](https://laravel.com/docs/7.x/eloquent#retrieving-and-updating-models)

onelinerhub: [How do I use the updateOrCreate method in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-updateorcreate-method-in-laravel-with-php)