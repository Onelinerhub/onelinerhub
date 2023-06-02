# How can I use PHPMailer without SMTP secure?
// plain

PHPMailer can be used without SMTP secure by using the mail() function. This function requires a local mail server to be installed and configured on the machine.

Here is an example of how to use PHPMailer without SMTP secure:

```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

//Set PHPMailer to use the mail() function
$mail->isMail();

//Set who the message is to be sent from
$mail->setFrom('from@example.com', 'First Last');

//Set who the message is to be sent to
$mail->addAddress('john@example.com', 'John Doe');

//Set the subject line
$mail->Subject = 'PHPMailer mail() test';

//Read an HTML message body from an external file, convert referenced images to embedded,
//convert HTML into a basic plain-text alternative body
$mail->msgHTML(file_get_contents('contents.html'), dirname(__FILE__));

//send the message, check for errors
if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}
?>
```

The code above will send an email using the mail() function of PHPMailer. It requires the `PHPMailerAutoload.php` file to be included first. Then, the `isMail()` method is used to set PHPMailer to use the mail() function. The `setFrom()` method is used to set the sender's address and name. The `addAddress()` method is used to set the recipient's address and name. The `Subject` property is used to set the subject of the email. The `msgHTML()` method is used to read the contents of an HTML message body from an external file. Finally, the `send()` method is used to send the message. If the message is sent successfully, it will output `Message sent!`.

Parts of the code:

- `require 'PHPMailerAutoload.php'`: This line is used to include the `PHPMailerAutoload.php` file.
- `$mail->isMail()`: This line is used to set PHPMailer to use the mail() function.
- `$mail->setFrom('from@example.com', 'First Last')`: This line is used to set the sender's address and name.
- `$mail->addAddress('john@example.com', 'John Doe')`: This line is used to set the recipient's address and name.
- `$mail->Subject = 'PHPMailer mail() test'`: This line is used to set the subject of the email.
- `$mail->msgHTML(file_get_contents('contents.html'), dirname(__FILE__))`: This line is used to read the contents of an HTML message body from an external file.
- `$mail->send()`: This line is used to send the message.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [How to Use PHPMailer Without SMTP](https://www.cloudways.com/blog/how-to-use-phpmailer-without-smtp/)

onelinerhub: [How can I use PHPMailer without SMTP secure?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-without-smtp-secure)