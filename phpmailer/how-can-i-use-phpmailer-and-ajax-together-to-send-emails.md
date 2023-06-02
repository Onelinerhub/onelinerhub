# How can I use PHPMailer and Ajax together to send emails?
// plain

PHPMailer is a library for sending emails from PHP. It can be used in combination with Ajax to send emails asynchronously.

Below is an example code snippet of how this can be done:
```
// Create the PHPMailer instance
$mail = new PHPMailer();

// Set the AJAX request parameters
$recipient = $_POST['recipient'];
$subject = $_POST['subject'];
$body = $_POST['body'];

// Set the PHPMailer parameters
$mail->setFrom('example@example.com', 'Example');
$mail->addAddress($recipient);
$mail->Subject = $subject;
$mail->Body = $body;

// Send the email
if($mail->send()) {
    echo 'Message has been sent';
} else {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

## Output example
 `Message has been sent`

## Code explanation


1. Create the PHPMailer instance - `$mail = new PHPMailer();`
2. Set the AJAX request parameters - `$recipient = $_POST['recipient'];` etc.
3. Set the PHPMailer parameters - `$mail->setFrom('example@example.com', 'Example');` etc.
4. Send the email - `if($mail->send()) { echo 'Message has been sent'; } else { echo 'Message could not be sent.'; echo 'Mailer Error: ' . $mail->ErrorInfo; }`

## Helpful links

- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [Ajax](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX)

onelinerhub: [How can I use PHPMailer and Ajax together to send emails?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-and-ajax-together-to-send-emails)