# How to use the Query Builder in PHP Symfony?
// plain

The Query Builder in PHP Symfony is a powerful tool for creating and executing database queries. It allows you to easily create complex SQL queries without having to write raw SQL.

## Example

```
$qb = $this->createQueryBuilder('u');
$qb->select('u.name')
   ->where('u.age > :age')
   ->setParameter('age', 18);
```

This example will generate the following SQL query:
```
SELECT u.name
FROM users u
WHERE u.age > 18
```

## Code explanation

- `$qb = $this->createQueryBuilder('u');` - creates a new query builder object
- `$qb->select('u.name')` - selects the `name` column from the `users` table
- `->where('u.age > :age')` - adds a `WHERE` clause to the query
- `->setParameter('age', 18)` - sets the `age` parameter to `18`

## Helpful links
- [Query Builder Documentation](https://symfony.com/doc/current/doctrine/query_builder.html)
- [Doctrine Documentation](https://www.doctrine-project.org/projects/doctrine-orm/en/2.7/reference/query-builder.html)

onelinerhub: [How to use the Query Builder in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-the-query-builder-in-php-symfony)