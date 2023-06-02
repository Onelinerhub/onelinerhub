# How do I configure PHPMailer to use Gmail OAuth authentication?
// plain

To configure PHPMailer to use Gmail OAuth authentication, you will need to have the latest version of PHPMailer installed.

You will also need to have the OAuth 2.0 Client library installed.

Once these are installed, you can use the following code to set up PHPMailer to use Gmail OAuth authentication:

```
require 'vendor/autoload.php';
$mail = new PHPMailerOAuth;
$mail->isSMTP();
$mail->SMTPDebug = 0;
$mail->Host = 'smtp.gmail.com';
$mail->Port = 587;
$mail->SMTPSecure = 'tls';
$mail->AuthType = 'XOAUTH2';
$mail->oauthUserEmail = 'your_gmail_address@gmail.com';
$mail->oauthClientId = 'your_client_id';
$mail->oauthClientSecret = 'your_client_secret';
$mail->oauthRefreshToken = 'your_refresh_token';
```

## Code explanation

- `require 'vendor/autoload.php';`: this line is used to include the autoload file from the OAuth 2.0 Client library.
- `$mail = new PHPMailerOAuth;`: this line creates a new instance of the PHPMailerOAuth class.
- `$mail->isSMTP();`: this line sets the mailer to use SMTP.
- `$mail->SMTPDebug = 0;`: this line sets the SMTP debugging level.
- `$mail->Host = 'smtp.gmail.com';`: this line sets the host to Gmail's SMTP server.
- `$mail->Port = 587;`: this line sets the SMTP port.
- `$mail->SMTPSecure = 'tls';`: this line sets the SMTP encryption type.
- `$mail->AuthType = 'XOAUTH2';`: this line sets the authentication type to OAuth 2.0.
- `$mail->oauthUserEmail = 'your_gmail_address@gmail.com';`: this line sets the Gmail address to use for authentication.
- `$mail->oauthClientId = 'your_client_id';`: this line sets the OAuth client ID.
- `$mail->oauthClientSecret = 'your_client_secret';`: this line sets the OAuth client secret.
- `$mail->oauthRefreshToken = 'your_refresh_token';`: this line sets the OAuth refresh token.

No output is produced.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [OAuth 2.0 Client Documentation](https://github.com/thephpleague/oauth2-client)

onelinerhub: [How do I configure PHPMailer to use Gmail OAuth authentication?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-gmail-oauth-authentication)