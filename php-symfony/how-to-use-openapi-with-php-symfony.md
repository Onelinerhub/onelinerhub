# How to use OpenAPI with PHP Symfony?
// plain

OpenAPI (formerly known as Swagger) is a popular framework for creating and documenting RESTful APIs. It can be used with PHP Symfony to create a powerful and easy-to-use API.

To use OpenAPI with PHP Symfony, you need to install the [NelmioApiDocBundle](https://github.com/nelmio/NelmioApiDocBundle) package.

Once installed, you can create a controller with the following code:

```php
<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Nelmio\ApiDocBundle\Annotation\Model;
use Nelmio\ApiDocBundle\Annotation\Security;
use Swagger\Annotations as SWG;

class MyController extends AbstractController
{
    /**
     * @SWG\Response(
     *     response=200,
     *     description="Returns a list of users",
     *     @SWG\Schema(
     *         type="array",
     *         @SWG\Items(ref=@Model(type=User::class))
     *     )
     * )
     * @SWG\Tag(name="users")
     * @Security(name="Bearer")
     */
    public function listUsers()
    {
        // ...
    }
}
```

This code will generate an OpenAPI document that describes the `listUsers` endpoint. The `@SWG\Response` annotation is used to define the response of the endpoint, the `@SWG\Tag` annotation is used to group related endpoints, and the `@Security` annotation is used to define the authentication method.

The generated OpenAPI document can then be used to generate client libraries for various languages, such as JavaScript, Python, and Java.

## Helpful links

- [NelmioApiDocBundle](https://github.com/nelmio/NelmioApiDocBundle)
- [OpenAPI Specification](https://swagger.io/specification/)

onelinerhub: [How to use OpenAPI with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-openapi-with-php-symfony)