# How can I catch and handle a PHPMailer exception?
// plain

Catching and handling a PHPMailer exception can be done using a `try/catch` statement.

For example:

```php
try {
    // code that may throw an exception
    $mail->send();
} catch (Exception $e) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

This will output:
```
Message could not be sent.
Mailer Error: SMTP connect() failed.
```

## Code explanation

- `try` - The try block contains the code that may throw an exception.
- `catch` - The catch block contains the code that will be executed when the exception is thrown.
- `Exception $e` - The `$e` variable is an instance of the `Exception` class that contains information about the exception that was thrown.
- `$mail->send()` - This is the code that may throw an exception.
- `echo 'Message could not be sent.'` - This code is executed if an exception is thrown.
- `echo 'Mailer Error: ' . $mail->ErrorInfo;` - This code is executed if an exception is thrown and will print the error message.

For more information, please see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting).

onelinerhub: [How can I catch and handle a PHPMailer exception?](https://onelinerhub.com/phpmailer/how-can-i-catch-and-handle-a-phpmailer-exception)