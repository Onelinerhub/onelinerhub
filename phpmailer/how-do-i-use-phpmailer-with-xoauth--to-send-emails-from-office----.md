# How do I use PHPMailer with XOAuth2 to send emails from Office 365?
// plain

To use PHPMailer with XOAuth2 to send emails from Office 365, you need to set up an application in Azure Active Directory. Once the application is set up, you can use the following code to authenticate with XOAuth2 and send an email:

```php
require 'vendor/autoload.php';

$mail = new PHPMailer;
$mail->isSMTP();
$mail->SMTPAuth = true;
$mail->Host = 'smtp.office365.com';
$mail->Port = 587;
$mail->SMTPSecure = 'tls';

$mail->AuthType = 'XOAUTH2';

$email = 'user@example.com';
$clientId = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx';
$clientSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';

$provider = new League\OAuth2\Client\Provider\GenericProvider([
    'clientId'                => $clientId,
    'clientSecret'            => $clientSecret,
    'redirectUri'             => 'https://example.com/callback-url',
    'urlAuthorize'            => 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize',
    'urlAccessToken'          => 'https://login.microsoftonline.com/common/oauth2/v2.0/token',
    'urlResourceOwnerDetails' => '',
    'scopes'                  => 'openid profile email'
]);

$mail->XOAuth2 = new PHPMailer\OAuth\OAuth2($provider, [
    'clientId' => $clientId,
    'clientSecret' => $clientSecret,
    'refreshToken' => 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'userName' => $email,
]);

$mail->setFrom($email, 'User');
$mail->addAddress('recipient@example.com', 'Recipient');
$mail->Subject = 'PHPMailer XOAuth2 Office365 Mail';
$mail->Body = 'This is a test email sent with PHPMailer and XOAuth2 authentication from Office365.';

if(!$mail->send()) {
    echo 'Mailer Error: '. $mail->ErrorInfo;
} else {
    echo 'Message sent!';
}
```

## Output example


```
Message sent!
```

The code above consists of the following parts:

1. Require the PHPMailer autoloader: `require 'vendor/autoload.php';`
2. Initialize the PHPMailer object: `$mail = new PHPMailer;`
3. Set up the SMTP connection:
    * `$mail->isSMTP();`
    * `$mail->SMTPAuth = true;`
    * `$mail->Host = 'smtp.office365.com';`
    * `$mail->Port = 587;`
    * `$mail->SMTPSecure = 'tls';`
4. Set the authentication type to XOAuth2: `$mail->AuthType = 'XOAUTH2';`
5. Set up the OAuth2 provider:
    * `$provider = new League\OAuth2\Client\Provider\GenericProvider([`
    * `'clientId' => $clientId,`
    * `'clientSecret' => $clientSecret,`
    * `'redirectUri' => 'https://example.com/callback-url',`
    * `'urlAuthorize' => 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize',`
    * `'urlAccessToken' => 'https://login.microsoftonline.com/common/oauth2/v2.0/token',`
    * `'urlResourceOwnerDetails' => '',`
    * `'scopes' => 'openid profile email'`
    * `]);`
6. Set up the XOAuth2 authentication:
    * `$mail->XOAuth2 = new PHPMailer\OAuth\OAuth2($provider, [`
    * `'clientId' => $clientId,`
    * `'clientSecret' => $clientSecret,`
    * `'refreshToken' => 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',`
    * `'userName' => $email,`
    * `]);`
7. Set up the email parameters:
    * `$mail->setFrom($email, 'User');`
    * `$mail->addAddress('recipient@example.com', 'Recipient');`
    * `$mail->Subject = 'PHPMailer XOAuth2 Office365 Mail';`
    * `$mail->Body = 'This is a test email sent with PHPMailer and XOAuth2 authentication from Office365.';`
8. Send the email: `$mail->send();`

## Helpful links

* [PHPMailer](https://github.com/PHPMailer/PHPMailer)
* [XOAuth2](https://github.com/PHPMailer/OAuth)
* [League OAuth2 Client](https://github.com/thephpleague/oauth2-client)
* [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/)

onelinerhub: [How do I use PHPMailer with XOAuth2 to send emails from Office 365?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-xoauth--to-send-emails-from-office----)