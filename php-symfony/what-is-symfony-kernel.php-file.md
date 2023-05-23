# What is Symfony Kernel.php file?
// plain

Symfony Kernel.php file is the heart of a Symfony application. It is responsible for bootstrapping the application and managing its configuration. It is a PHP class that extends the `Symfony\Component\HttpKernel\Kernel` class.

The Kernel class is responsible for:

- Registering bundles: Bundles are the main building blocks of a Symfony application. The Kernel class registers all the bundles that are needed for the application to run.

- Configuring the application: The Kernel class is responsible for loading the application configuration and making it available to the rest of the application.

- Initializing the application: The Kernel class is responsible for initializing the application and making it ready to handle requests.

## Example code

```php
<?php

use Symfony\Component\HttpKernel\Kernel;

class AppKernel extends Kernel
{
    public function registerBundles()
    {
        $bundles = array(
            // ...
        );

        return $bundles;
    }

    public function registerContainerConfiguration(LoaderInterface $loader)
    {
        $loader->load(__DIR__.'/config/config_'.$this->getEnvironment().'.yml');
    }
}
```

## Helpful links
- [Symfony Kernel Documentation](https://symfony.com/doc/current/components/http_kernel.html)
- [Symfony Bundles Documentation](https://symfony.com/doc/current/bundles.html)

onelinerhub: [What is Symfony Kernel.php file?](https://onelinerhub.com/php-symfony/what-is-symfony-kernel.php-file)