# How do I add a file to PHPMailer?
// plain

To add a file to PHPMailer, use the `addAttachment()` method. This method takes two parameters: the file path and the file name.

```php
$mail->addAttachment('/path/to/file.pdf', 'file.pdf');
```

The output of this code will be `true`, indicating that the file was successfully attached.

## Code explanation

- `addAttachment()`: The method used to add a file to PHPMailer.
- `'/path/to/file.pdf'`: The file path.
- `'file.pdf'`: The file name.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I add a file to PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-add-a-file-to-phpmailer)