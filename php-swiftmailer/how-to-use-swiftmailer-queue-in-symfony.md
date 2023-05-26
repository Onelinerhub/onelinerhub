# How to use Swiftmailer queue in Symfony?
// plain

Swiftmailer queue in Symfony can be used to send emails asynchronously. This can be done by creating a message queue and then using the Swiftmailer spool feature.

## Example code

```
$transport = new \Swift_SmtpTransport('smtp.example.org', 25);
$mailer = new \Swift_Mailer($transport);
$spool = new \Swift_MemorySpool();
$mailer->registerPlugin(new \Swift_Plugins_MessageLogger());
$mailer->registerPlugin(new \Swift_Plugins_SpoolTransportPlugin($spool));

$message = (new \Swift_Message('Hello Email'))
    ->setFrom(['john@doe.com' => 'John Doe'])
    ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
    ->setBody('Here is the message itself')
;

$mailer->send($message);
```

## Output example

```
Sent 1 emails
```

## Code explanation


1. Create a transport object with the SMTP server details:
```
$transport = new \Swift_SmtpTransport('smtp.example.org', 25);
```

2. Create a mailer object with the transport object:
```
$mailer = new \Swift_Mailer($transport);
```

3. Create a spool object:
```
$spool = new \Swift_MemorySpool();
```

4. Register the message logger and spool transport plugin with the mailer object:
```
$mailer->registerPlugin(new \Swift_Plugins_MessageLogger());
$mailer->registerPlugin(new \Swift_Plugins_SpoolTransportPlugin($spool));
```

5. Create a message object with the details of the email:
```
$message = (new \Swift_Message('Hello Email'))
    ->setFrom(['john@doe.com' => 'John Doe'])
    ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
    ->setBody('Here is the message itself')
;
```

6. Send the message using the mailer object:
```
$mailer->send($message);
```

## Helpful links

1. [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
2. [Symfony Documentation](https://symfony.com/doc/current/email.html)

onelinerhub: [How to use Swiftmailer queue in Symfony?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-queue-in-symfony)