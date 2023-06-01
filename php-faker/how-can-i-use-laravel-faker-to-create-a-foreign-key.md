# How can I use Laravel Faker to create a foreign key?
// plain

Using Laravel Faker to create a foreign key is a great way to generate fake data for your database. Here is an example of how you can do this:

```
$faker = Faker\Factory::create();

$userId = DB::table('users')->insertGetId([
    'name' => $faker->name,
    'email' => $faker->email
]);

DB::table('posts')->insert([
    'user_id' => $userId,
    'title' => $faker->sentence,
    'body' => $faker->paragraph
]);
```

In the example above, we create a new user with a name and email, and then store the ID of that user in the variable `$userId`. We then use that ID to create a new post in the posts table, and set the `user_id` column to the `$userId` variable. This creates a foreign key relationship between the users and posts tables.

## Code explanation


1. `$faker = Faker\Factory::create();` - This creates an instance of the Faker class.
2. `DB::table('users')->insertGetId([` - This inserts a new user into the users table, and returns the ID of the newly created user.
3. `'name' => $faker->name,` - This uses the Faker class to generate a fake name for the user.
4. `'user_id' => $userId,` - This sets the user_id column of the posts table to the ID of the newly created user.
5. `DB::table('posts')->insert([` - This inserts a new post into the posts table.
6. `$faker->sentence,` - This uses the Faker class to generate a fake title for the post.
7. `$faker->paragraph` - This uses the Faker class to generate a fake body for the post.

For more information on using Laravel Faker, please visit the [Laravel Faker documentation](https://github.com/fzaninotto/Faker#fakerprovideren).

onelinerhub: [How can I use Laravel Faker to create a foreign key?](https://onelinerhub.com/php-faker/how-can-i-use-laravel-faker-to-create-a-foreign-key)