# How can I use PHP Laravel and MongoDB together?
// plain

You can use PHP Laravel and MongoDB together by using the MongoDB PHP library. This library provides a set of classes and methods that allow you to interact with MongoDB from within your Laravel application.

For example, to insert a document into a MongoDB collection, you can use the `insertOne` method:
```
$collection->insertOne([
    'name' => 'John Doe',
    'age' => 30
]);
```

The above code will insert a document into the `$collection` MongoDB collection.

You can also query MongoDB collections using the `find` method:
```
$result = $collection->find([
    'name' => 'John Doe'
]);
```

The above code will return all documents in the `$collection` MongoDB collection that match the criteria specified in the query.

To learn more about using PHP Laravel and MongoDB together, check out the following links:

- [MongoDB PHP Library](https://docs.mongodb.com/php-library/)
- [Laravel MongoDB](https://laravel-mongodb.com/)
- [Using MongoDB with Laravel](https://www.cloudways.com/blog/using-mongodb-with-laravel/)

onelinerhub: [How can I use PHP Laravel and MongoDB together?](https://onelinerhub.com/php-laravel/how-can-i-use-php-laravel-and-mongodb-together)