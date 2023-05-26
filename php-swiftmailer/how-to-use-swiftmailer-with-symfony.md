# How to use Swiftmailer with Symfony?
// plain

Swiftmailer is a popular library for sending emails in Symfony applications. It is easy to use and provides a lot of features.

To use Swiftmailer with Symfony, first install the library using Composer:
```
composer require swiftmailer/swiftmailer
```

Then, configure the Swiftmailer settings in the `config/packages/swiftmailer.yaml` file:
```
swiftmailer:
    transport: '%env(MAILER_URL)%'
    username: '%env(MAILER_USERNAME)%'
    password: '%env(MAILER_PASSWORD)%'
```

Finally, create a service to send emails using Swiftmailer:
```
<?php

namespace App\Service;

use Swift_Mailer;

class Mailer
{
    private $mailer;

    public function __construct(Swift_Mailer $mailer)
    {
        $this->mailer = $mailer;
    }

    public function sendEmail($subject, $from, $to, $body)
    {
        $message = (new \Swift_Message($subject))
            ->setFrom($from)
            ->setTo($to)
            ->setBody($body);

        $this->mailer->send($message);
    }
}
```

## Code explanation

- `composer require swiftmailer/swiftmailer`: Installs the Swiftmailer library.
- `swiftmailer:`: Configures the Swiftmailer settings in the `config/packages/swiftmailer.yaml` file.
- `public function __construct(Swift_Mailer $mailer)`: Creates a service to send emails using Swiftmailer.
- `$message = (new \Swift_Message($subject))`: Creates a new Swift_Message instance.
- `$this->mailer->send($message)`: Sends the email.

## Helpful links
- [Swiftmailer Documentation](https://symfony.com/doc/current/email.html)
- [Swiftmailer GitHub Repository](https://github.com/swiftmailer/swiftmailer)

onelinerhub: [How to use Swiftmailer with Symfony?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-with-symfony)