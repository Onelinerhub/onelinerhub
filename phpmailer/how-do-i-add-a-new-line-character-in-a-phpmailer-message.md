# How do I add a new line character in a PHPMailer message?
// plain

Adding a new line character in PHPMailer message is quite simple. You can use the following example code block to do it:

```
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->Body = "This is the first line\nThis is the second line";

echo $mail->Body;
```

The output of the above code will be:
```
This is the first line
This is the second line
```

## Code explanation

- `require 'PHPMailerAutoload.php'`: This includes the PHPMailer library.
- `$mail = new PHPMailer`: This creates a new PHPMailer instance.
- `$mail->Body = "This is the first line\nThis is the second line"`: This sets the body of the message and adds a new line character (\n) between the two lines.
- `echo $mail->Body`: This outputs the body of the message.

## Helpful links
- [PHPMailer](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I add a new line character in a PHPMailer message?](https://onelinerhub.com/phpmailer/how-do-i-add-a-new-line-character-in-a-phpmailer-message)