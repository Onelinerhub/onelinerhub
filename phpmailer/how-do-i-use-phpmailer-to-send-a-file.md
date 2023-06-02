# How do I use PHPMailer to send a file?
// plain

PHPMailer is a library for sending emails in PHP. To use it to send a file, you will need to include the library, create an instance of the PHPMailer class, and then call the `addAttachment()` method.

## Example code

```
<?php
// Include the PHPMailer library
require_once('PHPMailer/class.phpmailer.php');

// Create an instance of the PHPMailer class
$mail = new PHPMailer();

// Set the from address
$mail->From = 'you@example.com';

// Set the to address
$mail->AddAddress('recipient@example.com');

// Set the subject
$mail->Subject = 'Here is the file you requested';

// Attach the file
$mail->addAttachment('/path/to/file.pdf');

// Send the email
$mail->Send();
```

No output is produced by this example code.

The code consists of four parts:
1. Including the PHPMailer library: `require_once('PHPMailer/class.phpmailer.php');`
2. Creating an instance of the PHPMailer class: `$mail = new PHPMailer();`
3. Setting the from and to addresses and the subject of the email: `$mail->From = 'you@example.com';` and `$mail->AddAddress('recipient@example.com');` and `$mail->Subject = 'Here is the file you requested';`
4. Attaching the file and sending the email: `$mail->addAttachment('/path/to/file.pdf');` and `$mail->Send();`

## Helpful links
- [PHPMailer Project Page](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I use PHPMailer to send a file?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-a-file)