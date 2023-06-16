# How do I roll back a Laravel migration using PHP?
// plain

You can roll back a Laravel migration using PHP by using the `artisan` command. `artisan` is the command-line interface included with Laravel.

To roll back a migration, you can use the `migrate:rollback` command. This command will roll back the last "batch" of migrations, which may include multiple migration files.

## Example

```
php artisan migrate:rollback
```

## Output example

```
Rolled back: 2019_08_19_000000_create_failed_jobs_table
```

This command will roll back the last batch of migrations, which may include multiple migration files. You can also specify a specific migration to roll back by using the `--step` option.

## Example

```
php artisan migrate:rollback --step=2
```

This command will roll back the last two migrations.

You can also roll back all of your migrations by using the `migrate:reset` command.

## Example

```
php artisan migrate:reset
```

This command will roll back all of your migrations.

## Code explanation

- `artisan` - command-line interface included with Laravel
- `migrate:rollback` - command to roll back the last "batch" of migrations
- `--step` - option to specify a specific migration to roll back
- `migrate:reset` - command to roll back all of your migrations

## Helpful links
- [Laravel Artisan Documentation](https://laravel.com/docs/7.x/artisan)
- [Laravel Migrations Documentation](https://laravel.com/docs/7.x/migrations)

onelinerhub: [How do I roll back a Laravel migration using PHP?](https://onelinerhub.com/php-laravel/how-do-i-roll-back-a-laravel-migration-using-php)