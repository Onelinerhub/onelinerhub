# How can I use DTOs in a Laravel PHP project?
// plain

DTOs (Data Transfer Objects) are objects that are used to transfer data between the application's layers. In a Laravel PHP project, they can be used to map data from the database to the application's domain objects.

For example, the following code block creates a DTO class that maps data from the `users` table:
```php
class UserDTO
{
    public $id;
    public $name;
    public $email;

    public function __construct($data)
    {
        $this->id = $data->id;
        $this->name = $data->name;
        $this->email = $data->email;
    }
}
```

The DTO can then be used to create a domain object:
```php
$userDTO = new UserDTO($data);
$user = new User($userDTO);
```

## Code explanation

- `UserDTO` class: maps data from the `users` table
- `__construct` method: assigns the data to the DTO's properties
- `$userDTO` variable: holds an instance of the DTO
- `$user` variable: holds an instance of the domain object

## Helpful links
- [Data Transfer Object Design Pattern](https://refactoring.guru/design-patterns/data-transfer-object)
- [Laravel - Eloquent: Getting Started](https://laravel.com/docs/7.x/eloquent#getting-started)

onelinerhub: [How can I use DTOs in a Laravel PHP project?](https://onelinerhub.com/php-laravel/how-can-i-use-dtos-in-a-laravel-php-project)