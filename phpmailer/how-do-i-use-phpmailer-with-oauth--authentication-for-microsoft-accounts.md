# How do I use PHPMailer with OAuth2 authentication for Microsoft accounts?
// plain

PHPMailer can be used with OAuth2 authentication for Microsoft accounts by following these steps:

1. Install the PHPMailer composer package.
2. Get the OAuth2 token from the Microsoft account.
3. Configure the PHPMailer object with the OAuth2 token.

## Example code

```
// Create a new PHPMailer instance
$mail = new PHPMailer;

// Set the OAuth2 access token
$mail->setOAuthToken($token);

// Set the from address
$mail->setFrom('from@example.com', 'First Last');

// Set the subject
$mail->Subject = 'PHPMailer OAuth2 Mail';

// Set the SMTP host
$mail->Host = 'smtp.example.com';

// Set the SMTP authentication type
$mail->SMTPAuthType = 'XOAUTH2';

// Send the message
$mail->send();
```

The above code will configure the PHPMailer object with the OAuth2 token and send the message using the SMTP authentication type `XOAUTH2`.

Parts of the code:
- `$mail = new PHPMailer;`: Creates a new PHPMailer instance.
- `$mail->setOAuthToken($token);`: Sets the OAuth2 access token.
- `$mail->setFrom('from@example.com', 'First Last');`: Sets the from address.
- `$mail->Subject = 'PHPMailer OAuth2 Mail';`: Sets the subject.
- `$mail->Host = 'smtp.example.com';`: Sets the SMTP host.
- `$mail->SMTPAuthType = 'XOAUTH2';`: Sets the SMTP authentication type.
- `$mail->send();`: Sends the message.

## Helpful links
- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)
- [Microsoft OAuth2 documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)

onelinerhub: [How do I use PHPMailer with OAuth2 authentication for Microsoft accounts?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-oauth--authentication-for-microsoft-accounts)