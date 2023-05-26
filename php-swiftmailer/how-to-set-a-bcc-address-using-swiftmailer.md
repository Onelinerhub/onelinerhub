# How to set a BCC address using Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in PHP. To set a BCC address using Swiftmailer, you can use the `addBcc()` method.

## Example code

```
$message = (new \Swift_Message('Hello World'))
  ->setFrom('john@example.com')
  ->setTo('jane@example.com')
  ->addBcc('bcc@example.com')
  ->setBody('Here is the message itself');
```

The code above will set the BCC address to `bcc@example.com`.

## Code explanation

- `\Swift_Message('Hello World')`: creates a new Swift_Message object with the subject "Hello World".
- `setFrom('john@example.com')`: sets the sender address to `john@example.com`.
- `setTo('jane@example.com')`: sets the recipient address to `jane@example.com`.
- `addBcc('bcc@example.com')`: adds the BCC address `bcc@example.com`.
- `setBody('Here is the message itself')`: sets the body of the message to "Here is the message itself".

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to set a BCC address using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-a-bcc-address-using-swiftmailer)