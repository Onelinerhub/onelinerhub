# How do I use a PHP fake mailer?
// plain

Using a PHP fake mailer is a way to send emails without using an actual email server. This can be useful for testing purposes or for sending emails without revealing the sender's identity.

To use a PHP fake mailer, you first need to include the `mail.php` library in your PHP script:
```php
require_once('mail.php');
```

Next, create an instance of the `mail` class and set the `From` and `To` fields to the desired email addresses:
```php
$mail = new mail;
$mail->From('from@example.com');
$mail->To('to@example.com');
```

Then, set the subject and body of the email:
```php
$mail->Subject('Hello World');
$mail->Body('This is a test email.');
```

Finally, call the `Send` method to send the email:
```php
$mail->Send();
```

If the email was sent successfully, the `Send` method will return `true`.

#### Code Parts Explanation

1. `require_once('mail.php');`: This includes the `mail.php` library in the PHP script.
2. `$mail = new mail;`: This creates an instance of the `mail` class.
3. `$mail->From('from@example.com');`: This sets the `From` field of the email to `from@example.com`.
4. `$mail->To('to@example.com');`: This sets the `To` field of the email to `to@example.com`.
5. `$mail->Subject('Hello World');`: This sets the subject of the email to `Hello World`.
6. `$mail->Body('This is a test email.');`: This sets the body of the email to `This is a test email.`.
7. `$mail->Send();`: This sends the email.

#### Relevant Links

- [PHP Fake Mailer Documentation](https://github.com/php-fake-mailer/php-fake-mailer)

onelinerhub: [How do I use a PHP fake mailer?](https://onelinerhub.com/php-faker/how-do-i-use-a-php-fake-mailer)