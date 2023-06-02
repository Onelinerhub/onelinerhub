# How can I create a fake mail script using PHP?
// plain

Creating a fake mail script using PHP is quite simple. The following example code will create a fake mail script that sends a message to a recipient:
```
<?php
$to = 'recipient@example.com';
$subject = 'Fake Mail Script';
$message = 'This is a fake mail script.';
$headers = 'From: sender@example.com' . "\r\n" .
    'Reply-To: sender@example.com' . "\r\n" .
    'X-Mailer: PHP/' . phpversion();

mail($to, $subject, $message, $headers);
?>
```
This code will send an email to the recipient with the subject "Fake Mail Script" and the message "This is a fake mail script."

The code consists of four parts:
1. `$to` - The recipient's email address.
2. `$subject` - The subject of the email.
3. `$message` - The body of the email.
4. `$headers` - Headers that are added to the email, such as the sender's address and the "X-Mailer" header.

Finally, the `mail()` function is used to send the email.

## Helpful links
- [PHP mail() Function](https://www.php.net/manual/en/function.mail.php)

onelinerhub: [How can I create a fake mail script using PHP?](https://onelinerhub.com/php-faker/how-can-i-create-a-fake-mail-script-using-php)