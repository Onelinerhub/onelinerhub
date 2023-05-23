# How to create a login page in PHP Symfony?
// plain

Creating a login page in PHP Symfony is a relatively simple process.

First, create a route in the `routing.yml` file:
```
login:
    path:     /login
    defaults: { _controller: AppBundle:Security:login }
```

Then, create a controller in the `SecurityController.php` file:
```
<?php

namespace AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;

class SecurityController extends Controller
{
    public function loginAction(Request $request)
    {
        // ...
    }
}
```

Next, create a form in the `login.html.twig` file:
```
<form action="{{ path('login') }}" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="_username" value="{{ last_username }}" />

    <label for="password">Password:</label>
    <input type="password" id="password" name="_password" />

    <button type="submit">login</button>
</form>
```

Finally, create a security check in the `SecurityController.php` file:
```
<?php

namespace AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Security\Http\Authentication\AuthenticationUtils;

class SecurityController extends Controller
{
    public function loginAction(Request $request, AuthenticationUtils $authUtils)
    {
        // get the login error if there is one
        $error = $authUtils->getLastAuthenticationError();

        // last username entered by the user
        $lastUsername = $authUtils->getLastUsername();

        return $this->render('security/login.html.twig', array(
            'last_username' => $lastUsername,
            'error'         => $error,
        ));
    }
}
```

## Code explanation


1. Route: `routing.yml` file
2. Controller: `SecurityController.php` file
3. Form: `login.html.twig` file
4. Security Check: `SecurityController.php` file

## Helpful links

- [Symfony Documentation - How to Create a Login Form](https://symfony.com/doc/current/security/form_login_setup.html)
- [Symfony Documentation - How to Create a Custom Login Form](https://symfony.com/doc/current/security/form_login_custom.html)

onelinerhub: [How to create a login page in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-a-login-page-in-php-symfony)