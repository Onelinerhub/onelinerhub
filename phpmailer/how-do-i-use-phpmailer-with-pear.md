# How do I use PHPMailer with PEAR?
// plain

PHPMailer and PEAR are two different packages that can be used together to send emails. PEAR is a package manager for PHP, while PHPMailer is a library that can be used to send emails. To use PHPMailer with PEAR, you need to install the PHPMailer package from PEAR.

To install PHPMailer from PEAR, you can use the following command:

```
pear install mail_mime
```

Once the package is installed, you can use the following example code to send an email using PHPMailer and PEAR:

```
<?php
require_once "Mail.php";

$from = "sender@example.com";
$to = "receiver@example.com";
$subject = "Test Email";
$body = "This is a test email sent using PHPMailer and PEAR.";

$host = "mail.example.com";
$port = "25";
$username = "sender@example.com";
$password = "password";

$headers = array ('From' => $from,
  'To' => $to,
  'Subject' => $subject);
$smtp = Mail::factory('smtp',
  array ('host' => $host,
    'port' => $port,
    'auth' => true,
    'username' => $username,
    'password' => $password));

$mail = $smtp->send($to, $headers, $body);

if (PEAR::isError($mail)) {
  echo("<p>" . $mail->getMessage() . "</p>");
} else {
  echo("<p>Message successfully sent!</p>");
}
?>
```

This code will send an email from the sender's address to the receiver's address, using the specified host, port, username, and password. If the email is successfully sent, it will output `Message successfully sent!`, otherwise it will output an error message.

## Code explanation
**
1. `pear install mail_mime` - This command is used to install the PHPMailer package from PEAR.
2. `require_once "Mail.php"` - This is used to include the PHPMailer library.
3. `$from`, `$to`, `$subject`, `$body` - These are variables used to store the sender's address, receiver's address, subject line, and body of the email.
4. `$host`, `$port`, `$username`, `$password` - These variables are used to store the host, port, username, and password used to authenticate the sender.
5. `$headers` - This is an array used to store the sender's address, receiver's address, and subject line.
6. `$smtp` - This is an object used to connect to the SMTP server.
7. `$mail` - This is an object used to send the email.
8. `PEAR::isError($mail)` - This is used to check for any errors when sending the email.

**## Helpful links**
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [PEAR Documentation](https://pear.php.net/manual/en/index.php)

onelinerhub: [How do I use PHPMailer with PEAR?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-pear)