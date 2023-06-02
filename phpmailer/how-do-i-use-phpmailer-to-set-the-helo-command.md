# How do I use PHPMailer to set the HELO command?
// plain

The [PHPMailer](https://github.com/PHPMailer/PHPMailer) library can be used to set the HELO command. The `$mail->Helo` method is used to set the name of the local machine.

For example:

```php
$mail->Helo = 'example.com';
```

This will set the HELO command to `example.com`.

## Code explanation


- `$mail`: This is an instance of the `PHPMailer` class.
- `->Helo`: This is the method used to set the HELO command.
- `'example.com'`: This is the value used to set the HELO command.

## Helpful links
- [GitHub - PHPMailer/PHPMailer: The classic email sending library for PHP](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I use PHPMailer to set the HELO command?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-set-the-helo-command)