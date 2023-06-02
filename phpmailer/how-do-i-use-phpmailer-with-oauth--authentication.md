# How do I use PHPMailer with OAuth2 authentication?
// plain

PHPMailer can be used with OAuth2 authentication using the OAuth2 class. This class provides a way to authenticate with an OAuth2 server, and then use that authentication to send emails using PHPMailer.

The following example code shows how to use PHPMailer with OAuth2 authentication:

```php
//Create an instance of PHPMailer
$mail = new PHPMailer;

//Tell PHPMailer to use SMTP
$mail->isSMTP();

//Create a new OAuth2 instance
$oauth = new OAuth2;

//Set the OAuth2 access token
$oauth->setToken('MY_OAUTH2_ACCESS_TOKEN');

//Set the OAuth2 authentication type
$mail->AuthType = 'XOAUTH2';

//Set the OAuth2 instance
$mail->oauthInstance = $oauth;

// Connect to the SMTP server
$mail->Host = 'smtp.example.com';

//Send the message
$mail->send();
```

This code will authenticate with the OAuth2 server using the provided access token, and then use that authentication to send the email using PHPMailer.

The code consists of the following parts:

1. Create an instance of PHPMailer.
2. Tell PHPMailer to use SMTP.
3. Create a new OAuth2 instance.
4. Set the OAuth2 access token.
5. Set the OAuth2 authentication type.
6. Set the OAuth2 instance.
7. Connect to the SMTP server.
8. Send the message.

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki) and the [OAuth2 documentation](https://oauth.net/2/).

onelinerhub: [How do I use PHPMailer with OAuth2 authentication?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-oauth--authentication)