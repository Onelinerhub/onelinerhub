# How can I use PHPMailer to copy an existing email?
// plain

PHPMailer can be used to copy an existing email by using the `addStringAttachment()` function. This function takes two parameters: the contents of the attachment and the filename. The contents of the attachment should be the raw source of the email, including all headers, that you want to copy.

For example:
```
$mail = new PHPMailer;
$mail->addStringAttachment($raw_email_source, 'email_copy.eml');
```

This will attach the email to the message as an .eml file.

The parts of the code are as follows:
- `$mail = new PHPMailer;`: This creates a new PHPMailer object.
- `addStringAttachment()`: This is the function used to attach the raw source of the email to the message.
- `$raw_email_source`: This is a string containing the raw source of the email.
- `'email_copy.eml'`: This is the filename of the attachment.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [addStringAttachment() Documentation](https://github.com/PHPMailer/PHPMailer/wiki/Using-the-addStringAttachment%28%29-method)

onelinerhub: [How can I use PHPMailer to copy an existing email?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-copy-an-existing-email)