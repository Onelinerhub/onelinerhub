# How do I get the message ID of a sent email using PHPMailer?
// plain

To get the message ID of a sent email using PHPMailer, you can use the `getLastMessageID()` method. This method returns the message ID of the most recently sent email.

## Example code

```
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

// your code to send email

echo $mail->getLastMessageID();
```

## Output example

```
<3.0.0.20160309173342.023a8c10@example.com>
```

This code does the following:
1. Includes the PHPMailerAutoload file.
2. Instantiates a new PHPMailer object.
3. Sends the email.
4. Echoes the message ID of the most recently sent email.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I get the message ID of a sent email using PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-get-the-message-id-of-a-sent-email-using-phpmailer)