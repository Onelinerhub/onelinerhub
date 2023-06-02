# How do I use PHPMailer to download a file?
// plain

PHPMailer is a library for sending emails in PHP. To use it to download a file, you need to first install the library using Composer:

```
composer require phpmailer/phpmailer
```

Then, you need to create an instance of the PHPMailer class and set up the parameters for your email:

```php
$mail = new PHPMailer();
$mail->Host = 'smtp.example.com';
$mail->Username = 'username';
$mail->Password = 'password';
$mail->addAddress('recipient@example.com');
```

After that, you can use the `addAttachment()` method to attach the file to the email:

```php
$mail->addAttachment('/path/to/file.zip');
```

Finally, you can send the email with the file attached using the `send()` method:

```php
$mail->send();
```

The recipient will then receive the email with the file attached, which they can download.

Parts of the Code:

1. `composer require phpmailer/phpmailer` - Installs the PHPMailer library
2. `$mail = new PHPMailer()` - Creates an instance of the PHPMailer class
3. `$mail->Host = 'smtp.example.com'` - Sets the host for sending the email
4. `$mail->Username = 'username'` - Sets the username for authentication
5. `$mail->Password = 'password'` - Sets the password for authentication
6. `$mail->addAddress('recipient@example.com')` - Sets the recipient's email address
7. `$mail->addAttachment('/path/to/file.zip')` - Attaches the file to the email
8. `$mail->send()` - Sends the email with the file attached

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Composer Documentation](https://getcomposer.org/doc/)

onelinerhub: [How do I use PHPMailer to download a file?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-download-a-file)