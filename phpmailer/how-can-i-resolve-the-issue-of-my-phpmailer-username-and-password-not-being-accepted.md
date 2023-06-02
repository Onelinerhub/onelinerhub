# How can I resolve the issue of my PHPmailer username and password not being accepted?
// plain

1. First, check that you have the correct username and password. Make sure that the credentials are correct and that the username is not an email address.
2. Check that the SMTP server is configured correctly, and that the correct port is being used. The default port for SMTP is usually 25, but this may vary.
3. If you are using Gmail as your SMTP server, you may need to enable less secure apps in your Google account settings. This can be done by logging into your Google account, going to the Security tab, and enabling less secure apps.
4. You may also need to enable the PHP mailer class in your php.ini file. To do this, you will need to add the following line to your php.ini file:
```
extension=php_openssl.dll
```
5. You may also need to enable TLS encryption in your PHPmailer configuration. To do this, you will need to add the following line to your PHPmailer configuration:
```
$mail->SMTPOptions = array(
'ssl' => array(
'verify_peer' => false,
'verify_peer_name' => false,
'allow_self_signed' => true
)
);
```
6. If you are still having issues, you can try using SMTP authentication instead of POP3 authentication. This can be done by setting the SMTPAuth property to true in your PHPmailer configuration.
7. You can also try using a different SMTP server, such as SendGrid or Amazon SES.

## Helpful links
* [PHPmailer Documentation](https://github.com/PHPMailer/PHPMailer)
* [Gmail Less Secure Apps](https://support.google.com/accounts/answer/6010255?hl=en)
* [SendGrid](https://sendgrid.com/)
* [Amazon SES](https://aws.amazon.com/ses/)

onelinerhub: [How can I resolve the issue of my PHPmailer username and password not being accepted?](https://onelinerhub.com/phpmailer/how-can-i-resolve-the-issue-of-my-phpmailer-username-and-password-not-being-accepted)