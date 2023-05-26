# How to get the error message in Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in PHP. To get the error message in Swiftmailer, you can use the `getErrors()` method. This method will return an array of errors that occurred while sending the email.

## Example code

```php
<?php
$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25);
$mailer = Swift_Mailer::newInstance($transport);

$message = Swift_Message::newInstance('Test Subject')
  ->setFrom(array('john@doe.com' => 'John Doe'))
  ->setTo(array('receiver@domain.org', 'other@domain.org' => 'A name'))
  ->setBody('Here is the message itself');

try {
  $result = $mailer->send($message);
} catch (Exception $e) {
  $errors = $mailer->getErrors();
  print_r($errors);
}
```

## Output example

```
Array
(
    [0] => Failed to authenticate on SMTP server with username "john@doe.com"
    [1] => SMTP server did not accept the password
)
```

The `getErrors()` method will return an array of errors that occurred while sending the email. The array will contain a description of the error that occurred. This can be used to debug any issues that may arise while sending emails.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to get the error message in Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-get-the-error-message-in-swiftmailer)