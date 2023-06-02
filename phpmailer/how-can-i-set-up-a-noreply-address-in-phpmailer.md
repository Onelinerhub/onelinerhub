# How can I set up a noreply address in PHPMailer?
// plain

To set up a noreply address in PHPMailer, you can use the following code block:

```
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->From = 'noreply@example.com'; //Set the "From" address
$mail->FromName = 'No Reply'; //Set the "From" name

//Add other mail settings

?>
```

This code block sets up the noreply address to be `noreply@example.com` with the "From" name set to `No Reply`. You can replace `example.com` with your own domain name.

You can also add other mail settings such as the SMTP settings, email body, and attachments.

The parts of the code are as follows:

1. `require 'PHPMailerAutoload.php';`: This line includes the PHPMailer library.
2. `$mail = new PHPMailer;`: This line creates a new instance of the PHPMailer class.
3. `$mail->From = 'noreply@example.com';`: This line sets the "From" address to `noreply@example.com`.
4. `$mail->FromName = 'No Reply';`: This line sets the "From" name to `No Reply`.

For more information, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I set up a noreply address in PHPMailer?](https://onelinerhub.com/phpmailer/how-can-i-set-up-a-noreply-address-in-phpmailer)