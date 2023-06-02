# How do I use PHPMailer to add an address?
// plain

Using PHPMailer to add an address is a simple process. Here is an example code block to illustrate how to do it:

```
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->addAddress('john@example.com', 'John Doe');

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

This code will add the address 'john@example.com' and name 'John Doe' to the recipient list. The `addAddress()` method takes two parameters: the email address and the name of the recipient. If the message is successfully sent, the output will be 'Message has been sent'.

The following are the parts of this code and their explanations:

- `require 'PHPMailerAutoload.php';` - This imports the PHPMailer library.
- `$mail = new PHPMailer;` - This creates a new PHPMailer instance.
- `$mail->addAddress('john@example.com', 'John Doe');` - This adds an address to the recipient list.
- `if(!$mail->send()) {...} else {...}` - This checks if the message is successfully sent and outputs an appropriate message.

Here are some relevant links to learn more about PHPMailer:

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [GitHub Repository for PHPMailer](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I use PHPMailer to add an address?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-add-an-address)