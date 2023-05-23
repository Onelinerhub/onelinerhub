# How to implement authentication with PHP Symfony?
// plain

Authentication with PHP Symfony can be implemented using the Security component. This component provides an authentication system that supports a variety of authentication mechanisms such as HTTP basic authentication, form login, and more.

## Example code

```
use Symfony\Component\Security\Core\Authentication\AuthenticationProviderManager;
use Symfony\Component\Security\Core\Authentication\Provider\DaoAuthenticationProvider;
use Symfony\Component\Security\Core\User\InMemoryUserProvider;

$userProvider = new InMemoryUserProvider(array(
    'admin' => array('password' => 'adminpass', 'roles' => array('ROLE_ADMIN')),
    'user' => array('password' => 'userpass', 'roles' => array('ROLE_USER')),
));

$authProvider = new DaoAuthenticationProvider($userProvider);

$authManager = new AuthenticationProviderManager(array($authProvider));
```

## Code explanation

- `InMemoryUserProvider`: This class provides an in-memory user provider. It stores users in an array and is used for testing purposes.
- `DaoAuthenticationProvider`: This class provides an authentication provider that uses a user provider to retrieve users and a user checker to check credentials.
- `AuthenticationProviderManager`: This class manages an array of authentication providers.

## Helpful links
- [Security Component Documentation](https://symfony.com/doc/current/components/security.html)
- [Authentication Provider Documentation](https://symfony.com/doc/current/security/authentication_provider.html)

onelinerhub: [How to implement authentication with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-implement-authentication-with-php-symfony)