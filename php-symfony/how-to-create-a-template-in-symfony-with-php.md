# How to create a template in Symfony with PHP?
// plain

Creating a template in Symfony with PHP is a simple process.

First, create a template file in the `templates` directory of your project. For example, `hello.html.php`:
```
<h1>Hello, <?= $name ?></h1>
```

Then, create a controller to render the template. For example, `HelloController.php`:
```
<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;

class HelloController extends AbstractController
{
    public function hello($name)
    {
        return $this->render('hello.html.php', [
            'name' => $name
        ]);
    }
}
```

Finally, add a route to the controller in `config/routes.yaml`:
```
hello:
    path: /hello/{name}
    controller: App\Controller\HelloController::hello
```

The output of the example code will be an HTML page with the text `Hello, [name]` where `[name]` is the value of the `$name` variable.

Parts of the code:
- `templates/hello.html.php`: Template file containing the HTML code to be rendered.
- `HelloController.php`: Controller class containing the logic to render the template.
- `config/routes.yaml`: Configuration file containing the route to the controller.

## Helpful links
- [Creating and Using Templates](https://symfony.com/doc/current/templates.html)
- [Routing](https://symfony.com/doc/current/routing.html)

onelinerhub: [How to create a template in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-create-a-template-in-symfony-with-php)