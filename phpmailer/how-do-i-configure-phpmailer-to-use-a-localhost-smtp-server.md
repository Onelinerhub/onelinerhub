# How do I configure PHPMailer to use a localhost SMTP server?
// plain

The following steps can be used to configure PHPMailer to use a localhost SMTP server:

1.  Include the PHPMailer library in your project, either by downloading and including the files directly, or by using a package manager such as Composer.

2. Set the `Host` property to the address of your localhost SMTP server.

```php
$mail->Host = 'localhost';
```

3. Set the `SMTPAuth` property to `true` to enable authentication.

```php
$mail->SMTPAuth = true;
```

4. Set the `Username` and `Password` properties to the credentials for your SMTP server.

```php
$mail->Username = 'username';
$mail->Password = 'password';
```

5. Set the `SMTPSecure` property to `tls` to enable TLS encryption.

```php
$mail->SMTPSecure = 'tls';
```

6. Set the `Port` property to the port number of your SMTP server.

```php
$mail->Port = 587;
```

7. Finally, call the `send()` method to send the email.

```php
$mail->send();
```

## Output example

```
true
```

Links:
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [Composer](https://getcomposer.org/)

onelinerhub: [How do I configure PHPMailer to use a localhost SMTP server?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-a-localhost-smtp-server)