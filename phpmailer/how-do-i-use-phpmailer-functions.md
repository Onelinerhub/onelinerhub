# How do I use PHPMailer functions?
// plain

PHPMailer is a library used to send emails from PHP. To use PHPMailer functions, you need to include the library in your code.

```
require 'PHPMailer/PHPMailerAutoload.php';
```

Then you can create a new PHPMailer instance, and set the necessary parameters like the recipient address, the sender address, the subject, etc.

```
$mail = new PHPMailer;
$mail->addAddress('recipient@example.com', 'Recipient Name');
$mail->setFrom('sender@example.com', 'Sender Name');
$mail->Subject = 'PHPMailer Test Subject';
```

You can also add content to the message body, such as HTML or plain text.

```
$mail->msgHTML(file_get_contents('contents.html'), __DIR__);
$mail->AltBody = 'This is a plain-text message body';
```

Finally, you can send the message using the `send()` method.

```
if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}
```

## Output example

```
Message sent!
```

For more information on how to use PHPMailer, please refer to the [documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How do I use PHPMailer functions?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-functions)