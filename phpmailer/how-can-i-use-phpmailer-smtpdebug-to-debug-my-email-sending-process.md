# How can I use PHPMailer SMTPDebug to debug my email sending process?
// plain

PHPMailer's SMTPDebug is a useful tool for debugging the email sending process. It allows you to see the SMTP conversation between the server and the client. To use it, set the SMTPDebug option to 2 in the PHPMailer object.

```
// Create a new PHPMailer object
$mail = new PHPMailer;

// Enable SMTPDebug
$mail->SMTPDebug = 2;
```

The output will look something like this:

```
SMTP -> FROM SERVER:220 smtp.example.com ESMTP Postfix
SMTP -> FROM SERVER: 250-smtp.example.com
SMTP -> FROM SERVER: 250-PIPELINING
SMTP -> FROM SERVER: 250-SIZE 10240000
SMTP -> FROM SERVER: 250-VRFY
SMTP -> FROM SERVER: 250-ETRN
SMTP -> FROM SERVER: 250-STARTTLS
SMTP -> FROM SERVER: 250-ENHANCEDSTATUSCODES
SMTP -> FROM SERVER: 250-8BITMIME
SMTP -> FROM SERVER: 250 DSN
SMTP -> FROM SERVER: 354 Enter message, ending with "." on a line by itself
SMTP -> FROM SERVER: 250 2.0.0 Ok: queued as 12345
```

The SMTPDebug option can be set to any of the following values:

* 0 = off (for production use)
* 1 = client messages
* 2 = client and server messages

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting).

onelinerhub: [How can I use PHPMailer SMTPDebug to debug my email sending process?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-smtpdebug-to-debug-my-email-sending-process)