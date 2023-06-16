# How do I use a transaction in PHP Laravel?
// plain

Using transactions in Laravel is a great way to ensure data integrity when dealing with multiple database operations. Transactions allow you to group multiple database operations into a single atomic operation, so that either all of the operations succeed, or none of them are applied.

To use a transaction in Laravel, you can use the `DB::transaction` method. This method accepts a closure which contains the database operations to be executed within the transaction. If any of the operations fail, then the transaction will be rolled back and none of the operations will be applied.

For example:
```php
DB::transaction(function () {
    DB::table('users')->update(['votes' => 1]);
    DB::table('posts')->delete();
});
```

The above code will update all users' `votes` to 1 and delete all posts in a single atomic operation. If either of the operations fail, then the transaction will be rolled back and none of the operations will be applied.

You can also use the `DB::beginTransaction` and `DB::commit` methods to manually start and commit a transaction.

For example:
```php
DB::beginTransaction();

try {
    DB::table('users')->update(['votes' => 1]);
    DB::table('posts')->delete();
    DB::commit();
} catch (\Exception $e) {
    DB::rollBack();
}
```

The above code will start a transaction, execute the two database operations, and then commit the transaction. If any of the operations fail, then the transaction will be rolled back.

## Helpful links
- [Laravel Database Transactions](https://laravel.com/docs/7.x/database#database-transactions)
- [PHP Manual: PDO::beginTransaction](https://www.php.net/manual/en/pdo.begintransaction.php)

onelinerhub: [How do I use a transaction in PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-use-a-transaction-in-php-laravel)