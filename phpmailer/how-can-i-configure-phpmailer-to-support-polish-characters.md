# How can I configure PHPMailer to support Polish characters?
// plain

To configure PHPMailer to support Polish characters, the following steps can be taken:

1. Set the character set to UTF-8:
```
$mail->CharSet = 'UTF-8';
```
2. Set the encoding to 8bit:
```
$mail->Encoding = '8bit';
```
3. Set the Content-Transfer-Encoding to 8bit:
```
$mail->ContentTransferEncoding = '8bit';
```
4. Set the Content-Type to text/plain:
```
$mail->ContentType = 'text/plain';
```
5. Set the language to Polish:
```
$mail->SetLanguage('pl');
```

These steps should allow PHPMailer to support Polish characters.

## Helpful links
* [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
* [PHPMailer Character Sets](https://github.com/PHPMailer/PHPMailer/wiki/Character-sets)
* [PHPMailer Languages](https://github.com/PHPMailer/PHPMailer/wiki/Language-Codes)

onelinerhub: [How can I configure PHPMailer to support Polish characters?](https://onelinerhub.com/phpmailer/how-can-i-configure-phpmailer-to-support-polish-characters)