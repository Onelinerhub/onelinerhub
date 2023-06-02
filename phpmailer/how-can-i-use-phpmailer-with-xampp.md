# How can I use PHPMailer with XAMPP?
// plain

PHPMailer is a PHP library that can be used to send emails from a web server. It can be used with XAMPP by following these steps:

1. Download the PHPMailer library from [GitHub](https://github.com/PHPMailer/PHPMailer).

2. Extract the downloaded file and copy the `PHPMailer` folder to the `XAMPP/htdocs` directory.

3. Create a PHP file in the `XAMPP/htdocs` directory and include the following code:

```
<?php
require 'PHPMailer/PHPMailerAutoload.php';

$mail = new PHPMailer;

//Your code here

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
?>
```

4. Configure the `$mail` object with the desired parameters such as `From`, `To`, `Subject`, `Body`, etc.

5. Execute the PHP file in the browser to send the email.

6. If the email is sent successfully, the output will be `Message has been sent`.

7. For more information, refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki).

onelinerhub: [How can I use PHPMailer with XAMPP?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-xampp)