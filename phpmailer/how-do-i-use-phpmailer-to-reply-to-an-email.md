# How do I use PHPMailer to reply to an email?
// plain

PHPMailer is a powerful library used for sending emails in PHP. To use it to reply to an email, you need to use the `addReplyTo()` method. This method takes two parameters: the email address and the name of the recipient.

For example:
```
$mail->addReplyTo('example@example.com', 'John Doe');
```

The code above will add a reply-to address to the email.

## Code explanation


- `$mail` - an instance of the PHPMailer class
- `addReplyTo()` - a method of the PHPMailer class used to add a reply-to address to the email
- `example@example.com` - the email address of the recipient
- `John Doe` - the name of the recipient

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I use PHPMailer to reply to an email?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-reply-to-an-email)