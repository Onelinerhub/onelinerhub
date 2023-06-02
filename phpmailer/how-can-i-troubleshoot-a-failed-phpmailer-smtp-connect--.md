# How can I troubleshoot a failed PHPMailer SMTP connect()?
// plain

1. Start by checking the debug output of PHPMailer. To do this, set the `SMTPDebug` property to `2` before calling `connect()`. This will provide detailed information about the connection process, such as any errors encountered.

```php
$mail->SMTPDebug = 2;
$mail->connect();
```

2. The debug output might provide information about why the connection is failing. For example, it might show that the SMTP server is refusing the connection due to invalid credentials.

3. If the debug output does not provide enough information, you can also try to connect to the SMTP server manually using the `fsockopen()` function. This will allow you to see the raw response from the server.

```php
$fp = fsockopen('smtp.example.com', 25);
if (!$fp) {
    echo "Could not open connection\n";
}
```

4. If the connection is successful, the server should respond with a string starting with `220`. If the connection is unsuccessful, it will respond with a different string.

5. Also check the `SMTPAuth` and `SMTPSecure` properties to make sure that they are set correctly for the server.

6. Make sure that the server is not blocking the connection from the IP address that you are using.

7. Finally, check the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer) for more information about troubleshooting SMTP connections.

onelinerhub: [How can I troubleshoot a failed PHPMailer SMTP connect()?](https://onelinerhub.com/phpmailer/how-can-i-troubleshoot-a-failed-phpmailer-smtp-connect--)