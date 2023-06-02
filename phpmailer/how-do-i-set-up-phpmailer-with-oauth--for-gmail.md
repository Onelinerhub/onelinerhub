# How do I set up PHPMailer with OAuth2 for Gmail?
// plain

1. First, you need to install PHPMailer via composer by running `composer require phpmailer/phpmailer` in your project's root folder.

2. Next, create a new Google project and enable the Gmail API in the Google API Console.

3. Create a new OAuth 2.0 Client ID and configure it for web application use.

4. Download the JSON file containing your Client ID and Client Secret and save it in your project's root folder.

5. Create the following PHP code to set up PHPMailer with OAuth2 for Gmail:

```
<?php
require 'vendor/autoload.php';

$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->Port = 587;
$mail->SMTPSecure = 'tls';
$mail->SMTPAuth = true;
$mail->AuthType = 'XOAUTH2';

$email = 'your_email@gmail.com';
$clientId = 'your_client_id.apps.googleusercontent.com';
$clientSecret = 'your_client_secret';

$refreshToken = 'your_refresh_token';

$provider = new League\OAuth2\Client\Provider\Google(
    array(
        'clientId' => $clientId,
        'clientSecret' => $clientSecret,
        'redirectUri' => '',
        'accessType' => 'offline'
    )
);

$mail->setOAuth(
    new OAuth(
        array(
            'provider' => $provider,
            'clientId' => $clientId,
            'clientSecret' => $clientSecret,
            'refreshToken' => $refreshToken,
            'userName' => $email,
        )
    )
);

$mail->From = $email;
$mail->FromName = 'Your Name';
$mail->addAddress('recipient@example.com', 'Recipient Name');

$mail->Subject = 'PHPMailer OAuth2 Gmail Test';
$mail->Body = 'This is a test using PHPMailer and OAuth2 for Gmail.';

if(!$mail->send()) {
    echo 'Message was not sent.';
    echo 'Mailer error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent.';
}
```

6. Replace `your_email@gmail.com`, `your_client_id.apps.googleusercontent.com`, `your_client_secret`, and `your_refresh_token` with the values from the JSON file.

7. Run the code to send the test email.

## Helpful links
- [PHPMailer Installation](https://github.com/PHPMailer/PHPMailer#installation)
- [Google API Console](https://console.developers.google.com/)
- [Creating OAuth 2.0 Client IDs](https://developers.google.com/identity/protocols/OAuth2#clientside)

onelinerhub: [How do I set up PHPMailer with OAuth2 for Gmail?](https://onelinerhub.com/phpmailer/how-do-i-set-up-phpmailer-with-oauth--for-gmail)