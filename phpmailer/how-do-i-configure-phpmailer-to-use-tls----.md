# How do I configure PHPMailer to use TLS 1.2?
// plain

1. Download and install PHPMailer.
2. Create a `PHPMailer` instance and set the `SMTPSecure` property to `'tls'`:
```
$mail = new PHPMailer;
$mail->SMTPSecure = 'tls';
```
3. Set the `SMTPAutoTLS` property to `true` to enable TLS 1.2:
```
$mail->SMTPAutoTLS = true;
```
4. Set the `Host` property to the SMTP hostname and port of your email provider:
```
$mail->Host = 'smtp.example.com:587';
```
5. Set the `SMTPAuth` property to `true` if your email provider requires authentication:
```
$mail->SMTPAuth = true;
```
6. Set the `Username` and `Password` properties if authentication is required:
```
$mail->Username = 'username';
$mail->Password = 'password';
```
7. Send the email using the `send()` method.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [PHPMailer Examples](https://github.com/PHPMailer/PHPMailer/tree/master/examples)

onelinerhub: [How do I configure PHPMailer to use TLS 1.2?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-tls----)