# How do I use PHPMailer to upload an avatar?
// plain

PHPMailer is a library for sending emails using PHP. To upload an avatar using PHPMailer, you need to use the `addAttachment()` method. This method takes two parameters: the path of the file and a name for the file.

## Example code

```
$mail->addAttachment('/path/to/avatar.jpg', 'avatar.jpg');
```

This code will add the file `avatar.jpg` located at `/path/to/avatar.jpg` as an attachment to the email.

The parts of this code are:
- `$mail`: This is an instance of the PHPMailer class.
- `addAttachment()`: This is the method used to add an attachment to the email.
- `'/path/to/avatar.jpg'`: This is the path of the file to be attached.
- `'avatar.jpg'`: This is the name of the file to be attached.

## Helpful links
- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [addAttachment() documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial#adding-attachments)

onelinerhub: [How do I use PHPMailer to upload an avatar?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-upload-an-avatar)