# How can I use Elasticsearch with Laravel?
// plain

Elasticsearch can be used with Laravel through the [Elasticquent](https://github.com/elasticquent/Elasticquent) package. This package provides a fluent syntax for mapping Eloquent models to Elasticsearch types.

To use Elasticquent, you first need to install it via composer:

```
composer require elasticquent/elasticquent
```

Once installed, you can create a model that extends the Elasticquent model. For example:

```php
use Elasticquent\ElasticquentTrait;

class User extends Model
{
    use ElasticquentTrait;

    protected $mappingProperties = [
        'name' => [
            'type' => 'string',
            'analyzer' => 'standard'
        ],
        'age' => [
            'type' => 'integer'
        ]
    ];
}
```

The `$mappingProperties` array contains the mapping information for the model. You can use this array to define the field types and other settings for the Elasticsearch type.

Once the model is created, you can use it to query the Elasticsearch index. For example, to search for users with a name of 'John':

```php
$users = User::searchByQuery(['match' => ['name' => 'John']]);
```

The `searchByQuery()` method takes a query array as an argument and returns an `ElasticquentResultCollection` object containing the results.

For more information, see the [Elasticquent documentation](https://github.com/elasticquent/Elasticquent).

onelinerhub: [How can I use Elasticsearch with Laravel?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-laravel)