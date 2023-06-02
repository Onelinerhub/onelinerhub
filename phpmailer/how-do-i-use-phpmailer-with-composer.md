# How do I use PHPMailer with Composer?
// plain

PHPMailer is a library for sending emails through PHP code. It can be easily installed via Composer, a PHP package manager.

To use PHPMailer with Composer, first you need to install the library. To do this, add the following line to the `composer.json` file:

```json
"phpmailer/phpmailer": "~6.0"
```

Then you need to run the `composer update` command in the terminal to install the library.

After that, you can use the library in your code. For example, you can create a new instance of the `PHPMailer` class and then set the `From` and `To` addresses and the `Subject` of the email:

```php
$mail = new PHPMailer;
$mail->setFrom('from@example.com', 'John Doe');
$mail->addAddress('to@example.com', 'Jane Doe');
$mail->Subject = 'Here is the subject';
```

You can also add the body of the email and send it:

```php
$mail->Body = 'This is the HTML message body <b>in bold!</b>';
$mail->send();
```

If the email was sent successfully, the output of the `send()` method will be `true`.

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md).

onelinerhub: [How do I use PHPMailer with Composer?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-composer)