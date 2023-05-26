# How to set multiple BCC addresses using Swiftmailer?
// plain

Swiftmailer can be used to set multiple BCC addresses in an email. To do this, the `addBcc()` method can be used. The following example code shows how to set multiple BCC addresses using Swiftmailer:

```
$message = (new \Swift_Message('Hello World'))
    ->setFrom('john@example.com')
    ->setTo('jane@example.com')
    ->addBcc('bob@example.com')
    ->addBcc('alice@example.com');
```

The output of the above code will be an email sent from `john@example.com` to `jane@example.com` with `bob@example.com` and `alice@example.com` as BCC recipients.

## Code explanation


- `$message`: This is a variable that stores the message object.
- `\Swift_Message('Hello World')`: This creates a new Swift_Message object with the subject line "Hello World".
- `setFrom('john@example.com')`: This sets the sender of the email to `john@example.com`.
- `setTo('jane@example.com')`: This sets the recipient of the email to `jane@example.com`.
- `addBcc('bob@example.com')`: This adds `bob@example.com` as a BCC recipient.
- `addBcc('alice@example.com')`: This adds `alice@example.com` as a BCC recipient.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to set multiple BCC addresses using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-multiple-bcc-addresses-using-swiftmailer)