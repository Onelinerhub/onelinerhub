# How can I troubleshoot a PHPMailer OpenSSL error?
// plain

1. First, check the version of OpenSSL installed on your server. This can be done by running the command `openssl version` from the command line.
2. If the version is not up to date, update it.
3. Check the `php.ini` file to make sure the `openssl` extension is enabled.
4. Make sure the `SMTP` settings are configured correctly in `PHPMailer`.
5. Test the connection using the `SMTP` class in `PHPMailer`:

```
require 'PHPMailerAutoload.php';
$mail = new PHPMailer();
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->Port = 587;
$mail->SMTPSecure = 'tls';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';

if (!$mail->smtpConnect()) {
    echo 'Connection failed!';
    echo '<pre>' . print_r($mail->getError(), true) . '</pre>';
} else {
    echo 'Connection successful!';
}
```

6. If the connection fails, check the error message for more information.
7. If necessary, consult the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting) for more troubleshooting tips.

onelinerhub: [How can I troubleshoot a PHPMailer OpenSSL error?](https://onelinerhub.com/phpmailer/how-can-i-troubleshoot-a-phpmailer-openssl-error)