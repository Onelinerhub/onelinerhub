# How do I use PHPMailer with Joomla?
// plain

PHPMailer is a library for sending emails using PHP. It can be used with Joomla to send emails from within a Joomla component or module.

To use PHPMailer with Joomla, first you need to include the PHPMailer library in your Joomla component or module. This can be done by adding the following code to your component or module:

```php
require_once JPATH_ROOT . '/libraries/phpmailer/PHPMailerAutoload.php';
```

Once the library is included, you can create an instance of the PHPMailer class and set the necessary email parameters such as the sender, recipient, subject, body, etc.

For example:

```php
$mailer = new PHPMailer;
$mailer->From = 'sender@example.com';
$mailer->AddAddress('recipient@example.com');
$mailer->Subject = 'Test Email';
$mailer->Body = 'This is a test email.';
```

Finally, you can send the email by calling the `Send()` method:

```php
if (!$mailer->Send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mailer->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

## Output example


```
Message has been sent
```

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Using PHPMailer with Joomla](https://docs.joomla.org/Using_PHPMailer_with_Joomla)

onelinerhub: [How do I use PHPMailer with Joomla?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-joomla)