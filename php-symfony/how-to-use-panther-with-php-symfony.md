# How to use Panther with PHP Symfony?
// plain

Panther is a library for testing web applications in PHP, and it can be used with Symfony.

To use Panther with Symfony, you need to install the Panther library and the Symfony Panther Bridge.

```
composer require symfony/panther
```

Then, you can create a test class that extends the PantherTestCase class.

```
<?php

namespace App\Tests;

use Symfony\Component\Panther\PantherTestCase;

class ExampleTest extends PantherTestCase
{
    public function testExample()
    {
        // ...
    }
}
```

You can then use the PantherTestCase class to create a client, navigate to a page, and interact with the page.

```
$client = static::createPantherClient();
$crawler = $client->request('GET', '/');
$link = $crawler->selectLink('About')->link();
$crawler = $client->click($link);
```

For more information, see the [Symfony Panther documentation](https://symfony.com/doc/current/testing/panther.html).

onelinerhub: [How to use Panther with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-panther-with-php-symfony)