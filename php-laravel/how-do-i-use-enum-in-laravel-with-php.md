# How do I use Enum in Laravel with PHP?
// plain

Enum is a data type that allows you to define a set of named constants. It can be used in Laravel with PHP to create an enumeration of values.

Here is an example of how to use Enum in Laravel with PHP:

```
<?php

namespace App;

use MyCLabs\Enum\Enum;

class UserType extends Enum
{
    const ADMIN = 'admin';
    const USER = 'user';
}

$userType = new UserType(UserType::USER);
echo $userType;

```

The output of this code will be `user`.

The code consists of the following parts:

1. A `namespace` statement to specify the namespace of the Enum class.
2. An `use` statement to import the Enum class from the MyCLabs\Enum package.
3. A class extending the Enum class to define the constants.
4. An instance of the UserType class initialized with the constant `USER`.
5. An `echo` statement to output the value of the constant.

For more information on using Enum in Laravel with PHP, see the following links:

- [PHP Enum Tutorial](https://www.sitepoint.com/php-enums-tutorial/)
- [MyCLabs/Enum](https://github.com/myclabs/php-enum)
- [Laravel Enums](https://github.com/BenSampo/laravel-enum)

onelinerhub: [How do I use Enum in Laravel with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-enum-in-laravel-with-php)