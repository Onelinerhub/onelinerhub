# How do I set the "From" field in PHPMailer?
// plain

The "From" field in PHPMailer is set using the `setFrom()` method. Here is an example of how to use this method:

```php
$mail->setFrom('from@example.com', 'From Name');
```

The `setFrom()` method takes two parameters: an email address and a name. The email address is a required parameter while the name is optional.

## Code explanation


- `$mail`: This is a PHPMailer object instance.
- `setFrom()`: This is the method used to set the "From" field.
- `from@example.com`: This is the email address used for the "From" field.
- `From Name`: This is the name used for the "From" field.

Here are some ## Helpful links

- [GitHub - PHPMailer/PHPMailer: The classic email sending library for PHP](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Docs - setFrom](https://github.com/PHPMailer/PHPMailer/blob/master/docs/methods/setFrom.md)

onelinerhub: [How do I set the "From" field in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-set-the--from--field-in-phpmailer)