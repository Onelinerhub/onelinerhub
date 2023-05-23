# How to do a health check in PHP Symfony?
// plain

A health check in PHP Symfony can be done using the [HealthCheckBundle](https://github.com/symfony/health-check). This bundle provides a way to check the health of your application by running a set of checks.

The following example code will run a health check and output the result:

```php
use Symfony\Component\HealthCheck\HealthCheck;

$healthCheck = new HealthCheck();
$result = $healthCheck->run();

echo $result->getStatus();
```

The code above will output either `healthy` or `unhealthy` depending on the result of the health check.

The HealthCheck class provides a set of methods to add checks to the health check. For example, the following code will add a check to check if a database connection is available:

```php
use Symfony\Component\HealthCheck\HealthCheck;
use Symfony\Component\HealthCheck\Check\DatabaseCheck;

$healthCheck = new HealthCheck();
$healthCheck->add(new DatabaseCheck('database_name'));
$result = $healthCheck->run();

echo $result->getStatus();
```

The HealthCheckBundle also provides a way to add custom checks. For more information, please refer to the [documentation](https://symfony.com/doc/current/components/health_check.html).

onelinerhub: [How to do a health check in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-do-a-health-check-in-php-symfony)