# How do I use PHPMailer with OAuth 2.0?
// plain

PHPMailer can be used with OAuth 2.0 for secure authentication and authorization. To do this, you must first obtain the necessary credentials from your email provider.

Once you have the credentials, you can use the following example code to authenticate with OAuth 2.0:

```php
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->SMTPSecure = 'ssl';
$mail->Port = 465;
$mail->Username = 'your_username';
$mail->Password = 'your_password';
$mail->AuthType = 'XOAUTH2';
$mail->oauthUserEmail = 'your_email_address';
$mail->oauthClientId = 'your_client_id';
$mail->oauthClientSecret = 'your_client_secret';
$mail->oauthRefreshToken = 'your_refresh_token';
```

This code sets up the SMTP connection and then authenticates with OAuth 2.0 using the credentials you obtained from your email provider.

## Code explanation

- `$mail`: An instance of the PHPMailer class.
- `$mail->isSMTP()`: Sets the mailer to use SMTP.
- `$mail->Host`: The SMTP server.
- `$mail->SMTPAuth`: Enables SMTP authentication.
- `$mail->SMTPSecure`: Sets the encryption system.
- `$mail->Port`: Sets the SMTP port.
- `$mail->Username`: The SMTP username.
- `$mail->Password`: The SMTP password.
- `$mail->AuthType`: The type of authentication.
- `$mail->oauthUserEmail`: The email address used for authentication.
- `$mail->oauthClientId`: The client ID obtained from the email provider.
- `$mail->oauthClientSecret`: The client secret obtained from the email provider.
- `$mail->oauthRefreshToken`: The refresh token obtained from the email provider.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [Gmail OAuth 2.0 Setup](https://developers.google.com/gmail/api/quickstart/php)

onelinerhub: [How do I use PHPMailer with OAuth 2.0?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-oauth----)