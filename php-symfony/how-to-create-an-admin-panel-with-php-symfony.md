# How to create an admin panel with PHP Symfony?
// plain

Creating an admin panel with PHP Symfony is a straightforward process.

First, create a new Symfony project:
```
composer create-project symfony/website-skeleton my_project
```

Then, install the EasyAdminBundle:
```
composer require admin
```

Next, configure the bundle in the `config/packages/easy_admin.yaml` file:
```
easy_admin:
    design:
        menu:
            # ...
        # ...
    # ...
```

Finally, create the admin controller and define the entities to manage:
```
<?php

namespace App\Controller;

use EasyCorp\Bundle\EasyAdminBundle\Controller\AbstractCrudController;

class AdminController extends AbstractCrudController
{
    public static function getEntityFqcn(): string
    {
        return YourEntity::class;
    }
    // ...
}
```

You can find more information about creating an admin panel with PHP Symfony in the [official documentation](https://symfony.com/doc/current/bundles/EasyAdminBundle/index.html).

onelinerhub: [How to create an admin panel with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-an-admin-panel-with-php-symfony)