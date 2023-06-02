# How do I debug a PHPmailer script?
// plain

Debugging a PHPmailer script can be done in several ways.

First, you can use a `try/catch` statement to catch exceptions that may occur in the script. For example:
```
try {
    // code
} catch (Exception $e) {
    echo 'Caught exception: ',  $e->getMessage(), "\n";
}
```

Second, you can use the `SMTPDebug` property to enable debugging messages. This will output verbose messages that can help you identify the cause of the issue. For example:
```
$mail->SMTPDebug = 2;
```

Third, you can use the `addCustomHeader` method to add custom headers to the email, which can help you debug the email. For example:
```
$mail->addCustomHeader('X-MyHeader', 'MyValue');
```

Finally, you can use the `getSMTPInstance` method to get an instance of the SMTP class, which can be used to debug the SMTP connection. For example:
```
$smtp = $mail->getSMTPInstance();
$smtp->do_debug = 3;
```

These techniques can be used to debug your PHPmailer script.

## Helpful links
* [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/tree/master/docs)
* [PHP Exception Handling](https://www.php.net/manual/en/language.exceptions.php)

onelinerhub: [How do I debug a PHPmailer script?](https://onelinerhub.com/phpmailer/how-do-i-debug-a-phpmailer-script)