# How do I set the boundary in PHPMailer?
// plain

PHPMailer is a library for sending emails. It can be used to set the boundary of an email, which is a string of characters that separates the different parts of the email.

To set the boundary in PHPMailer, you need to use the `$mail->createHeader()` method. This method takes two parameters, the first one being a string that contains the boundary string, and the second one being an array of headers.

## Example code

```php
$boundary = md5(time());
$mail->createHeader('Content-Type', ['boundary' => $boundary]);
```

The `$boundary` variable should be set to a unique string that is used to separate the different parts of the email. The `md5()` function is used to generate a unique string based on the current time.

The `$mail->createHeader()` method takes two parameters. The first parameter is a string that contains the boundary string. The second parameter is an array of headers, which is used to set the Content-Type header. The boundary string is set as a key in the array of headers.

## Helpful links
- https://github.com/PHPMailer/PHPMailer
- https://github.com/PHPMailer/PHPMailer/blob/master/class.phpmailer.php#L1399

onelinerhub: [How do I set the boundary in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-set-the-boundary-in-phpmailer)