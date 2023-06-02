# How do I set the from name when using PHPMailer?
// plain

The `From` name when using PHPMailer can be set using the `setFrom` method. This method takes two parameters, the address and the name.

## Example code

```php
$mail->setFrom('example@example.com', 'Example Name');
```

The `setFrom` method can also be used with an array containing the address and name.

## Example code

```php
$mail->setFrom(array('example@example.com' => 'Example Name'));
```

The `From` name can also be set using the `FromName` property.

## Example code

```php
$mail->FromName = 'Example Name';
```

The `From` name can also be set using the `addReplyTo` method. This method takes two parameters, the address and the name.

## Example code

```php
$mail->addReplyTo('example@example.com', 'Example Name');
```

The `From` name can also be set using the `Sender` property.

## Example code

```php
$mail->Sender = 'example@example.com';
```

The `From` name can also be set using the `addCustomHeader` method. This method takes two parameters, the header name and the header value.

## Example code

```php
$mail->addCustomHeader('From', 'Example Name <example@example.com>');
```

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [PHPMailer Examples](https://github.com/PHPMailer/PHPMailer/tree/master/examples)

onelinerhub: [How do I set the from name when using PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-set-the-from-name-when-using-phpmailer)