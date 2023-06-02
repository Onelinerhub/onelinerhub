# How do I set the content-type to text/html in PHPMailer?
// plain

In order to set the content-type to text/html in PHPMailer, you need to use the `isHTML()` method. This method takes a boolean value as a parameter, where `true` indicates that the content is HTML, and `false` indicates that the content is plain text. For example:

```php
$mail->isHTML(true);
```

The output of this code is nothing, since it is a method that sets a flag.

## Code explanation

- `$mail` - An instance of PHPMailer
- `isHTML()` - Method of PHPMailer that sets the content-type
- `true` - Parameter passed to `isHTML()` to indicate that the content is HTML

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I set the content-type to text/html in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-set-the-content-type-to-text-html-in-phpmailer)