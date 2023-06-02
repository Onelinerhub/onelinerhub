# How can I send emails using PHPMailer without using SMTP?
// plain

PHPMailer can be used to send emails without using SMTP by using the mail() function. The mail() function is a built-in PHP function that allows you to send emails directly from a script.

Here is an example of how to use the mail() function with PHPMailer:

```
<?php
    // Import the PHPMailer class
    use PHPMailer\PHPMailer\PHPMailer;

    // Create a new PHPMailer object
    $mail = new PHPMailer;

    // Set the from address
    $mail->setFrom('from@example.com', 'Sender Name');

    // Set the to address
    $mail->addAddress('to@example.com', 'Receiver Name');

    // Set the subject
    $mail->Subject = 'Test Email';

    // Set the body of the email
    $mail->Body = 'This is a test email!';

    // Send the email using the mail() function
    $mail->send();
?>
```

No output is produced when using the mail() function.

The code above does the following:

1. Imports the PHPMailer class.
2. Creates a new PHPMailer object.
3. Sets the from address.
4. Sets the to address.
5. Sets the subject.
6. Sets the body of the email.
7. Sends the email using the mail() function.

For more information on using PHPMailer without SMTP, please see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial).

onelinerhub: [How can I send emails using PHPMailer without using SMTP?](https://onelinerhub.com/phpmailer/how-can-i-send-emails-using-phpmailer-without-using-smtp)