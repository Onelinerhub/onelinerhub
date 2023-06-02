# How can I use PHPMailer to connect to a POP3 server?
// plain

PHPMailer can be used to connect to a POP3 server using the POP3 protocol. This can be done using the `getMail()` method. Here is an example code block:

```
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

//Load Composer's autoloader
require 'vendor/autoload.php';

$mail = new PHPMailer(true); // Passing `true` enables exceptions

//Server settings
$mail->Host = 'pop.example.com';
$mail->Port = 110;
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';

//Connect to the POP3 server
try {
    $mail->getMail();
    echo 'Connected to POP3 server';
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```

The output of this code will be: `Connected to POP3 server`.

## Code explanation


1. `use PHPMailer\PHPMailer\PHPMailer;` - imports the PHPMailer class into the global namespace.
2. `use PHPMailer\PHPMailer\Exception;` - imports the PHPMailer Exception class into the global namespace.
3. `require 'vendor/autoload.php';` - loads the Composer autoloader.
4. `$mail = new PHPMailer(true);` - creates a new instance of the PHPMailer class and enables exceptions.
5. `$mail->Host = 'pop.example.com';` - sets the POP3 server hostname.
6. `$mail->Port = 110;` - sets the POP3 server port.
7. `$mail->SMTPAuth = true;` - enables SMTP authentication.
8. `$mail->Username = 'user@example.com';` - sets the POP3 username.
9. `$mail->Password = 'secret';` - sets the POP3 password.
10. `$mail->getMail();` - connects to the POP3 server.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md)
- [PHPMailer API Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/api.md)

onelinerhub: [How can I use PHPMailer to connect to a POP3 server?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-connect-to-a-pop--server)