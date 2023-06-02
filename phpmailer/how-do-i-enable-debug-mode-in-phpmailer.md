# How do I enable debug mode in PHPMailer?
// plain

Debug mode in PHPMailer can be enabled by setting the `SMTPDebug` property. This property is available on the `PHPMailer` class and can be set to any of the following values:

- `0`: No debug output
- `1`: Commands
- `2`: Data and commands
- `3`: As 2 plus connection status
- `4`: Low-level data output

## Example code

```
// Enable SMTP debugging
// 0 = off (for production use)
// 1 = client messages
// 2 = client and server messages
$mail->SMTPDebug = 2;
```

## Output example

```
SERVER -> CLIENT: 220 smtp.example.com ESMTP Postfix
CLIENT -> SERVER: EHLO localhost
SERVER -> CLIENT: 250-smtp.example.com
SERVER -> CLIENT: 250-PIPELINING
SERVER -> CLIENT: 250-SIZE 10240000
SERVER -> CLIENT: 250-VRFY
SERVER -> CLIENT: 250-ETRN
SERVER -> CLIENT: 250-STARTTLS
SERVER -> CLIENT: 250-ENHANCEDSTATUSCODES
SERVER -> CLIENT: 250-8BITMIME
SERVER -> CLIENT: 250 DSN
```

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki/Troubleshooting)
- [SMTP Debugging in PHPMailer](https://www.sitepoint.com/sending-emails-php-phpmailer/)

onelinerhub: [How do I enable debug mode in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-enable-debug-mode-in-phpmailer)