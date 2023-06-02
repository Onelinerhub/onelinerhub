# How do I use PHPMailer to add an image as an attachment?
// plain

Using PHPMailer to add an image as an attachment is a simple process. Here is an example of code that can be used to do this:

```
<?php
    require 'PHPMailerAutoload.php';
    $mail = new PHPMailer;
    $mail->addAttachment('path/to/image.jpg');
?>
```

The code above will add an image as an attachment to the email. The addAttachment() function takes two parameters, the first is the path to the image and the second is an optional name that can be used to rename the attachment.

## Code explanation

1. `require 'PHPMailerAutoload.php';` - This line includes the PHPMailer library in the code.
2. `$mail = new PHPMailer;` - This line instantiates a new PHPMailer object.
3. `$mail->addAttachment('path/to/image.jpg');` - This line adds an image as an attachment to the email.

Here are some relevant links that can provide more information about using PHPMailer:
* [PHPMailer Official Documentation](https://github.com/PHPMailer/PHPMailer)
* [How to Send an Email with PHPMailer](https://www.w3schools.com/php/func_mail_phpmailer.asp)

onelinerhub: [How do I use PHPMailer to add an image as an attachment?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-add-an-image-as-an-attachment)