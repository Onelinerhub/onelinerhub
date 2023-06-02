# How can I use Laravel Faker to generate test data for my website?
// plain

Laravel Faker is a popular library used to generate fake data for testing purposes. It can be used to generate test data for a website by creating dummy records in the database. Here is an example code block to generate a dummy user:

```
$user = \App\User::create([
    'name' => \Faker\Factory::create()->name,
    'email' => \Faker\Factory::create()->safeEmail,
    'password' => bcrypt('password'),
]);
```

This code will generate a dummy user record, with a random name, safe email address and a bcrypt-hashed password.

## Code explanation


1. `\App\User::create([` - This is the Eloquent model used to create the user record.
2. `'name' => \Faker\Factory::create()->name` - This is the Faker factory used to generate a random name.
3. `'email' => \Faker\Factory::create()->safeEmail` - This is the Faker factory used to generate a safe email address.
4. `'password' => bcrypt('password')` - This is a bcrypt-hashed version of the password ‘password’.

## Helpful links

- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderbase)
- [Laravel Eloquent Documentation](https://laravel.com/docs/5.7/eloquent)

onelinerhub: [How can I use Laravel Faker to generate test data for my website?](https://onelinerhub.com/php-faker/how-can-i-use-laravel-faker-to-generate-test-data-for-my-website)