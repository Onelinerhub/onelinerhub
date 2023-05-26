# How to use Swiftmailer with Amazon SES?
// plain

Swiftmailer is a popular PHP library for sending emails. It can be used with Amazon SES (Simple Email Service) to send emails from your application.

To use Swiftmailer with Amazon SES, you need to configure the transport layer of Swiftmailer to use Amazon SES. This can be done by setting the `transport` option to `AmazonSesTransport` and providing the necessary credentials.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('email-smtp.us-east-1.amazonaws.com', 587, 'tls'))
  ->setUsername('YOUR_AMAZON_SES_USERNAME')
  ->setPassword('YOUR_AMAZON_SES_PASSWORD');

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Send the message
$result = $mailer->send($message);

// Print the result
echo $result;
```

## Output example

```
1
```

The code above configures the transport layer of Swiftmailer to use Amazon SES and sends an email using the `$message` object. The result of the `send()` method is the number of successful recipients.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Amazon SES Documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)

onelinerhub: [How to use Swiftmailer with Amazon SES?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-with-amazon-ses)