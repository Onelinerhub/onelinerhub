# How do I use PHPMailer with XOAuth2 authentication?
// plain

Using PHPMailer with XOAuth2 authentication is relatively easy. First, you need to install the PHPMailer library and the OAuth library.

```
# Install PHPMailer
composer require phpmailer/phpmailer

# Install OAuth
composer require league/oauth2-client
```

Once you have the libraries installed, you will need to get the OAuth credentials from the email service provider. You will need the Client ID, Client Secret, and Refresh Token.

Then, you can configure the PHPMailer object to use XOAuth2 authentication.

```
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
$mail->SMTPDebug = 2;

$mail->AuthType = 'XOAUTH2';
$mail->oauthUserEmail = 'user@example.com';
$mail->oauthClientId = 'CLIENT_ID';
$mail->oauthClientSecret = 'CLIENT_SECRET';
$mail->oauthRefreshToken = 'REFRESH_TOKEN';
```

Finally, you can send the email using the `send()` method.

```
$mail->setFrom('user@example.com');
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Test Email';
$mail->Body = 'This is a test email sent using PHPMailer and XOAuth2 authentication.';

if ($mail->send()) {
    echo 'Message sent!';
} else {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

## Output example

```
Message sent!
```

## Code Parts Explanation

- `composer require phpmailer/phpmailer`: Installs the PHPMailer library.
- `composer require league/oauth2-client`: Installs the OAuth library.
- `$mail->isSMTP()`: Sets the mailer to use SMTP protocol.
- `$mail->Host`: Sets the SMTP server address.
- `$mail->SMTPAuth`: Sets SMTP authentication.
- `$mail->SMTPSecure`: Sets the security system to use.
- `$mail->Port`: Sets the SMTP port.
- `$mail->SMTPDebug`: Sets SMTP debug mode.
- `$mail->AuthType`: Sets the authentication type.
- `$mail->oauthUserEmail`: Sets the user's email address.
- `$mail->oauthClientId`: Sets the OAuth client ID.
- `$mail->oauthClientSecret`: Sets the OAuth client secret.
- `$mail->oauthRefreshToken`: Sets the OAuth refresh token.
- `$mail->setFrom()`: Sets the sender's address.
- `$mail->addAddress()`: Sets the recipient's address.
- `$mail->Subject`: Sets the email subject.
- `$mail->Body`: Sets the email body.
- `$mail->send()`: Sends the email.

## Relevant Links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [OAuth Documentation](https://oauth.net/2/)

onelinerhub: [How do I use PHPMailer with XOAuth2 authentication?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-xoauth--authentication)