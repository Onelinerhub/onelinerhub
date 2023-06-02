# How do I add a logo to a PHPMailer message?
// plain

To add a logo to a PHPMailer message, you need to embed the logo image as an attachment and also reference it in the message body. Here is an example code block that demonstrates how to do this:

```php
//Create a new PHPMailer instance
$mail = new PHPMailer;

//Embed the logo image as an attachment
$mail->AddEmbeddedImage('/path/to/logo.jpg', 'logo_id', 'logo.jpg');

//Set the body of the message
$mail->Body = '<html><body>
<p>Here is an embedded logo: <img src="cid:logo_id" alt="Logo"/></p>
</body></html>';

//Send the message
$mail->Send();
```

This code will embed the logo image as an attachment and reference it in the message body using the `cid` scheme. The `AddEmbeddedImage` method takes three parameters; the first is the path to the image file, the second is an identifier that will be used to reference the image in the message body, and the third is the name of the image file.

## Code explanation


- `$mail = new PHPMailer;` - Creates a new PHPMailer instance
- `$mail->AddEmbeddedImage('/path/to/logo.jpg', 'logo_id', 'logo.jpg');` - Embeds the logo image as an attachment
- `$mail->Body = '<html><body>...</body></html>';` - Sets the body of the message
- `$mail->Send();` - Sends the message

For more information on using PHPMailer, please refer to the [official documentation](https://github.com/PHPMailer/PHPMailer/wiki).

onelinerhub: [How do I add a logo to a PHPMailer message?](https://onelinerhub.com/phpmailer/how-do-i-add-a-logo-to-a-phpmailer-message)