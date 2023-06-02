# How do I troubleshoot PHPmailer when it hangs?
// plain

1. First, check the configuration of your PHPmailer instance. Make sure the `$mail->Host` and `$mail->Port` parameters are correct.

2. Check the authentication settings for the mail server. Make sure the `$mail->Username` and `$mail->Password` are correct.

3. Check the `$mail->SMTPDebug` parameter to see if it is set to `2` or higher. This will enable verbose debugging output, which will help you identify the source of the issue.

4. Check the `$mail->SMTPSecure` parameter to make sure it is set correctly.

5. Check the `$mail->SMTPAutoTLS` parameter to make sure it is set to `true`.

6. Check the `$mail->SMTPOptions` array to make sure it is set correctly.

7. If the above steps do not help, try running the following code to see if the connection is successful:
```php
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->Port = 587;
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';

// Enable verbose debug output
$mail->SMTPDebug = 2;

if (!$mail->smtpConnect()) {
    echo 'Connection failed!';
} else {
    echo 'Connection successful!';
}
```
## Output example
 `Connection successful!`

onelinerhub: [How do I troubleshoot PHPmailer when it hangs?](https://onelinerhub.com/phpmailer/how-do-i-troubleshoot-phpmailer-when-it-hangs)