# How do I use PHPMailer to add a BCC recipient?
// plain

To use PHPMailer to add a BCC recipient, you can use the `addBCC()` method. This method takes two parameters - the email address of the recipient, and an optional name for the recipient.

## Example code

```
$mail = new PHPMailer;
$mail->addBCC('bcc@example.com', 'John Doe');
```

The code above will add a BCC recipient with the email address `bcc@example.com` and the name `John Doe`.

## Code explanation

- `$mail = new PHPMailer;` - creates a new instance of the PHPMailer class.
- `$mail->addBCC('bcc@example.com', 'John Doe');` - adds a BCC recipient with the email address `bcc@example.com` and the name `John Doe`.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How do I use PHPMailer to add a BCC recipient?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-add-a-bcc-recipient)