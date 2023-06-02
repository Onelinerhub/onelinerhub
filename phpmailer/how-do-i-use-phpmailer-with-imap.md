# How do I use PHPMailer with IMAP?
// plain

PHPMailer is an open-source library for sending emails from PHP. It provides an easy-to-use interface for sending emails with IMAP, a mail protocol used for accessing email on a remote server.

To use PHPMailer with IMAP, you need to first create an instance of PHPMailer and then set the host, port, username, and password for the IMAP server.

```php
<?php
// Create a new PHPMailer instance
$mail = new PHPMailer;

// Set the IMAP host
$mail->Host = 'imap.example.com';

// Set the IMAP port
$mail->Port = 993;

// Set the IMAP username
$mail->Username = 'username@example.com';

// Set the IMAP password
$mail->Password = 'password';

// Connect to the IMAP server
$mail->connect();

// Output: true
echo $mail->isConnected();
?>
```

## Output example
 `true`

The code above:

- Creates a new instance of PHPMailer (`$mail = new PHPMailer;`)
- Sets the host, port, username, and password for the IMAP server (`$mail->Host`, `$mail->Port`, `$mail->Username`, `$mail->Password`)
- Connects to the IMAP server (`$mail->connect()`)
- Outputs the result of the connection (`echo $mail->isConnected()`)

For more information on using PHPMailer with IMAP, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Using-IMAP).

onelinerhub: [How do I use PHPMailer with IMAP?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-imap)