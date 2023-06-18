# How can I use Sphinx search on Laravel?
// plain

Sphinx Search can be used with Laravel through the [Laravel-Sphinx](https://github.com/rtconner/laravel-sphinx) package. This package provides a SphinxQL query builder for Laravel, which allows for more efficient and expressive search queries.

To install the package, you can use the following command:

```
composer require rtconner/laravel-sphinx
```

Once installed, you can use the `SphinxQL` class to create query objects. These query objects can be used to search your Sphinx index. For example, the following code will search for any records with the word “Laravel” in the title field:

```
$results = SphinxQL::query()
    ->select('*')
    ->from('index_name')
    ->where('title', '=', 'Laravel')
    ->execute();
```

The `$results` variable will contain an array of objects that match the search query. The `SphinxQL` class also provides other methods for more complex search queries, such as `whereIn()` and `whereBetween()`.

For more detailed information on using Sphinx Search with Laravel, please refer to the following links:

* [Laravel-Sphinx Documentation](https://github.com/rtconner/laravel-sphinx/blob/master/README.md)
* [Laravel Documentation](https://laravel.com/docs/7.x/sphinx)
* [Sphinx Documentation](http://sphinxsearch.com/docs/)

onelinerhub: [How can I use Sphinx search on Laravel?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-on-laravel)