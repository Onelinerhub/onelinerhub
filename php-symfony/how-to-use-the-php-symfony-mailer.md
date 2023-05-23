# How to use the PHP Symfony mailer?
// plain

The PHP Symfony mailer is a library that allows you to send emails from your Symfony application. It is easy to use and provides a lot of flexibility.

## Example code

```
use Symfony\Component\Mailer\Mailer;
use Symfony\Component\Mailer\Transport\Smtp\EsmtpTransport;

$transport = new EsmtpTransport('smtp.example.com', 25);
$mailer = new Mailer($transport);

$email = (new TemplatedEmail())
    ->from('sender@example.com')
    ->to('recipient@example.com')
    ->subject('Hello!')
    ->htmlTemplate('emails/hello.html.twig')
    ->context(['name' => 'John Doe']);

$mailer->send($email);
```

This example code will send an email from `sender@example.com` to `recipient@example.com` with the subject `Hello!` and the HTML template `emails/hello.html.twig` with the context variable `name` set to `John Doe`.

## Code explanation

- `use Symfony\Component\Mailer\Mailer;`: imports the Mailer class from the Symfony Mailer library
- `use Symfony\Component\Mailer\Transport\Smtp\EsmtpTransport;`: imports the EsmtpTransport class from the Symfony Mailer library
- `$transport = new EsmtpTransport('smtp.example.com', 25);`: creates a new EsmtpTransport object with the SMTP server `smtp.example.com` and port `25`
- `$mailer = new Mailer($transport);`: creates a new Mailer object with the EsmtpTransport object
- `$email = (new TemplatedEmail())`: creates a new TemplatedEmail object
- `->from('sender@example.com')`: sets the sender of the email to `sender@example.com`
- `->to('recipient@example.com')`: sets the recipient of the email to `recipient@example.com`
- `->subject('Hello!')`: sets the subject of the email to `Hello!`
- `->htmlTemplate('emails/hello.html.twig')`: sets the HTML template of the email to `emails/hello.html.twig`
- `->context(['name' => 'John Doe'])`: sets the context variable `name` to `John Doe`
- `$mailer->send($email);`: sends the email

## Helpful links
- [Symfony Mailer Documentation](https://symfony.com/doc/current/mailer.html)

onelinerhub: [How to use the PHP Symfony mailer?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-mailer)