# tables

How do I use Yajra data tables with Laravel and PHP?
// plain

Yajra DataTables is a library that allows developers to easily create dynamic, interactive tables with sorting, searching, and pagination features in Laravel and PHP. To use Yajra DataTables with Laravel and PHP, first install the package via Composer:

```
composer require yajra/laravel-datatables-oracle
```

Then, add the service provider to your `config/app.php` file:

```
'providers' => [
    ...
    Yajra\DataTables\DataTablesServiceProvider::class,
],
```

Finally, publish the config file with:

```
php artisan vendor:publish --tag=datatables
```

Once the package is installed, you can create a data table by creating a new controller and adding the `DataTables` trait to it:

```php
use Yajra\DataTables\DataTables;

class MyController extends Controller
{
    use DataTables;
    ...
}
```

Then, you can create a route and a method to handle the data table request, and pass your Eloquent model to the `dataTable()` method:

```php
public function getDataTable()
{
    return datatables()->of(MyModel::query())->toJson();
}
```

This will return a JSON response with the data that can be used to populate your data table.

**Parts of example code:**

1. `composer require yajra/laravel-datatables-oracle` - This installs the Yajra DataTables package via Composer.
2. `Yajra\DataTables\DataTablesServiceProvider::class` - This adds the service provider to the `config/app.php` file.
3. `php artisan vendor:publish --tag=datatables` - This publishes the config file.
4. `use Yajra\DataTables\DataTables;` - This adds the `DataTables` trait to the controller.
5. `datatables()->of(MyModel::query())->toJson()` - This creates the data table and returns a JSON response with the data.

**## Helpful links**

- [Yajra DataTables Documentation](https://yajrabox.com/docs/laravel-datatables/master)
- [Laravel Documentation](https://laravel.com/docs)

onelinerhub: [tables

How do I use Yajra data tables with Laravel and PHP?](https://onelinerhub.com/php-laravel/tables--how-do-i-use-yajra-data-tables-with-laravel-and-php)