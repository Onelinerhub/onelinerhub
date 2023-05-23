# How to use the PHP Symfony findBy method?
// plain

The `findBy` method is a part of the Symfony Doctrine Query Builder and is used to query the database for specific records. It takes an array of parameters and returns an array of objects that match the criteria.

## Example

```
$users = $this->getDoctrine()
    ->getRepository(User::class)
    ->findBy(
        array('name' => 'John'),
        array('age' => 'ASC')
    );
```

## Output example

```
Array
(
    [0] => User Object
        (
            [name] => John
            [age] => 25
        )

    [1] => User Object
        (
            [name] => John
            [age] => 30
        )
)
```

## Code explanation

- `$this->getDoctrine()`: This is a method of the Symfony Controller class that returns the Doctrine object.
- `->getRepository(User::class)`: This is a method of the Doctrine object that returns the repository for the specified entity.
- `->findBy(array('name' => 'John'), array('age' => 'ASC'))`: This is a method of the repository that takes an array of parameters and returns an array of objects that match the criteria.

## Helpful links
- [Doctrine Query Builder](https://symfony.com/doc/current/doctrine/query_builder.html)
- [Symfony Controller](https://symfony.com/doc/current/controller.html)

onelinerhub: [How to use the PHP Symfony findBy method?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-findby-method)