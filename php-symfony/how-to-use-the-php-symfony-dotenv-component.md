# How to use the PHP Symfony Dotenv component?
// plain

The PHP Symfony Dotenv component is a library that allows developers to store configuration information in environment variables. It is used to keep sensitive information such as passwords and API keys out of source code.

## Example code

```
use Symfony\Component\Dotenv\Dotenv;

$dotenv = new Dotenv();
$dotenv->load(__DIR__.'/.env');
```

This code will load the environment variables from the `.env` file in the current directory.

## Code explanation

- `use Symfony\Component\Dotenv\Dotenv;` - imports the Dotenv class
- `$dotenv = new Dotenv();` - creates a new instance of the Dotenv class
- `$dotenv->load(__DIR__.'/.env');` - loads the environment variables from the `.env` file in the current directory

## Helpful links
- [GitHub - symfony/dotenv: Loads environment variables from .env to getenv(), $_ENV and $_SERVER automagically](https://github.com/symfony/dotenv)
- [Symfony - Configuring Symfony Applications](https://symfony.com/doc/current/configuration.html#configuring-symfony-applications)

onelinerhub: [How to use the PHP Symfony Dotenv component?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-dotenv-component)