# How to send an email using PHP in WordPress?
// plain

Sending an email using PHP in WordPress is a simple process. The following example code block can be used to send an email using PHP in WordPress:
```
<?php
$to = 'example@example.com';
$subject = 'Test Email';
$body = 'This is a test email sent using PHP in WordPress.';
$headers = array('Content-Type: text/html; charset=UTF-8');

wp_mail( $to, $subject, $body, $headers );
?>
```
The output of the example code is a successful email sent to the specified address.

## Code explanation


1. `$to`: This is the email address of the recipient.
2. `$subject`: This is the subject of the email.
3. `$body`: This is the body of the email.
4. `$headers`: This is an array of headers to be sent with the email.
5. `wp_mail()`: This is the WordPress function used to send the email.

## Helpful links

- [wp_mail() | WordPress Developer Resources](https://developer.wordpress.org/reference/functions/wp_mail/)

onelinerhub: [How to send an email using PHP in WordPress?](https://onelinerhub.com/php-wordpress/how-to-send-an-email-using-php-in-wordpress)