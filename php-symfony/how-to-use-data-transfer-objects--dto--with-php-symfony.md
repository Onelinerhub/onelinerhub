# How to use Data Transfer Objects (DTO) with PHP Symfony?
// plain

Data Transfer Objects (DTOs) are used to transfer data between layers of an application. In PHP Symfony, DTOs are used to transfer data between the controller and the view.

## Example code

```
// src/DTO/UserDTO.php

namespace App\DTO;

class UserDTO
{
    public $name;
    public $email;
}

// src/Controller/UserController.php

namespace App\Controller;

use App\DTO\UserDTO;

class UserController
{
    public function showUser(User $user)
    {
        $userDTO = new UserDTO();
        $userDTO->name = $user->getName();
        $userDTO->email = $user->getEmail();

        return $this->render('user.html.twig', [
            'user' => $userDTO
        ]);
    }
}
```

## Output example

```
Rendered user.html.twig with user data
```

## Code explanation

- `src/DTO/UserDTO.php`: This file contains the definition of the UserDTO class, which is used to store the user data.
- `src/Controller/UserController.php`: This file contains the showUser() method, which is used to retrieve the user data from the database and store it in a UserDTO object. The UserDTO object is then passed to the view.

## Helpful links
- [Data Transfer Objects (DTOs) in Symfony](https://symfony.com/doc/current/best_practices/business-logic.html#data-transfer-objects)

onelinerhub: [How to use Data Transfer Objects (DTO) with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-data-transfer-objects--dto--with-php-symfony)