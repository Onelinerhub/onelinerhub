# How do I use PHPMailer to send an HTML email with UTF-8 encoding?
// plain

Using PHPMailer to send an HTML email with UTF-8 encoding requires the following steps:

1. Include the PHPMailer library in your project:
```
require 'PHPMailer/src/PHPMailer.php';
```

2. Create a new PHPMailer instance:
```
$mail = new PHPMailer;
```

3. Set the character encoding to UTF-8:
```
$mail->CharSet = 'UTF-8';
```

4. Set the HTML content type:
```
$mail->isHTML(true);
```

5. Set the body of the email to the HTML content:
```
$mail->Body = '<h1>Hello World!</h1>';
```

6. Finally, send the email:
```
$mail->send();
```

7. Check for errors:
```
if ($mail->ErrorInfo) {
    echo 'Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message sent!';
}
```

**Output**: `Message sent!`

For more information, please refer to [PHPMailer's official documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How do I use PHPMailer to send an HTML email with UTF-8 encoding?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-an-html-email-with-utf---encoding)