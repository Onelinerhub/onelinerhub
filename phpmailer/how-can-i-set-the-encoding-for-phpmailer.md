# How can I set the encoding for PHPMailer?
// plain

To set the encoding for PHPMailer, you need to use the `$mail->CharSet` property. This property sets the character set used in the message. You can set it to either `utf-8` or `iso-8859-1`.

## Example code

```php
$mail->CharSet = 'utf-8';
```

The above code will set the character set to utf-8.

## Code explanation

- `$mail` - This is the PHPMailer object.
- `CharSet` - This is the property used to set the character set.
- `utf-8` - This is the character set used in the message.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md)

onelinerhub: [How can I set the encoding for PHPMailer?](https://onelinerhub.com/phpmailer/how-can-i-set-the-encoding-for-phpmailer)