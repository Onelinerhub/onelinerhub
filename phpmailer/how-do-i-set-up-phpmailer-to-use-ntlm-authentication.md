# How do I set up PHPMailer to use NTLM authentication?
// plain

PHPMailer can be configured to use NTLM authentication with the following steps:

1. Install the [ntlm_sasl](https://github.com/eustasy/ntlm_sasl) library by running `composer require eustasy/ntlm_sasl`

2. Create a new instance of the PHPMailer class and set the mailer to `smtp`

```php
$mail = new PHPMailer();
$mail->isSMTP();
```

3. Set the SMTP authentication type to `NTLM`

```php
$mail->AuthType = 'NTLM';
```

4. Set the SMTP host

```php
$mail->Host = 'smtp.example.com';
```

5. Set the SMTP username and password

```php
$mail->Username = 'username';
$mail->Password = 'password';
```

6. Set the NTLM authentication type

```php
$mail->AuthType = 'NTLM';
```

7. Finally, send the email

```php
$mail->send();
```

For more information on how to use PHPMailer with NTLM authentication, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/NTLM_authentication.md).

onelinerhub: [How do I set up PHPMailer to use NTLM authentication?](https://onelinerhub.com/phpmailer/how-do-i-set-up-phpmailer-to-use-ntlm-authentication)