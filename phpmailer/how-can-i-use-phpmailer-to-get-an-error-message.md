# How can I use PHPMailer to get an error message?
// plain

PHPMailer is a library for sending emails using the PHP language. To get an error message, you need to create a PHPMailer object and use the `setFrom()` and `addAddress()` methods to specify the sender and recipient. Then use the `send()` method to send the email. The `send()` method will return a boolean value of `true` if the email was sent successfully and `false` if there was an error.

## Example code

```
<?php
    require 'PHPMailerAutoload.php';

    $mail = new PHPMailer;

    $mail->setFrom('sender@example.com', 'Sender Name');
    $mail->addAddress('recipient@example.com', 'Recipient Name');

    if(!$mail->send()) {
        echo 'Message could not be sent.';
        echo 'Mailer Error: ' . $mail->ErrorInfo;
    } else {
        echo 'Message has been sent';
    }
?>
```

## Output example

```
Message could not be sent.
Mailer Error: SMTP connect() failed
```

Parts of the code and explanation:

1. `require 'PHPMailerAutoload.php';` - This line includes the PHPMailer library so that it can be used in the script.

2. `$mail = new PHPMailer;` - This line creates a new PHPMailer object.

3. `$mail->setFrom('sender@example.com', 'Sender Name');` - This line sets the sender's email address and name.

4. `$mail->addAddress('recipient@example.com', 'Recipient Name');` - This line sets the recipient's email address and name.

5. `if(!$mail->send()) {` - This line checks if the email was sent successfully. If it was not, it will return `false` and execute the code in the `if` block.

6. `echo 'Mailer Error: ' . $mail->ErrorInfo;` - This line prints out the error message.

## Helpful links
* [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How can I use PHPMailer to get an error message?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-get-an-error-message)