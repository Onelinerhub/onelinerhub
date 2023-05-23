# How to create a REST API with PHP Symfony?
// plain

Creating a REST API with PHP Symfony is a straightforward process.

First, create a new Symfony project:
```
composer create-project symfony/website-skeleton my_project
```

Then, install the necessary packages:
```
composer require symfony/webpack-encore-pack
composer require symfony/maker-bundle --dev
```

Next, create the controller and routes for the API:
```
php bin/console make:controller
```

Then, create the model and repository for the API:
```
php bin/console make:entity
```

Finally, configure the serializer to return the data in the desired format:
```
use Symfony\Component\Serializer\Serializer;
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;

$encoders = [new JsonEncoder()];
$normalizers = [new ObjectNormalizer()];

$serializer = new Serializer($normalizers, $encoders);

$jsonContent = $serializer->serialize($data, 'json');
```

The output of the serializer will be a JSON string containing the data from the model.

## Helpful links
- [Symfony Documentation](https://symfony.com/doc/current/index.html)
- [Creating a REST API with Symfony](https://symfony.com/doc/current/create_framework/rest_api.html)

onelinerhub: [How to create a REST API with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-a-rest-api-with-php-symfony)