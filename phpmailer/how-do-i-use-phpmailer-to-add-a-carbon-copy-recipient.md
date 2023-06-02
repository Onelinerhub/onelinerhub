# How do I use PHPMailer to add a carbon copy recipient?
// plain

Using PHPMailer to add a carbon copy recipient is very simple. All you need to do is add a line of code to your existing PHPMailer script.

```
$mail->addCC('cc@example.com');
```
This line of code will add a carbon copy recipient to your email.

The code above consists of two parts:
1. `$mail->addCC('cc@example.com');` - This is the command used to add a carbon copy recipient.
2. `cc@example.com` - This is the email address of the carbon copy recipient.

No output is generated when this code is executed.

For more information, please see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial).

onelinerhub: [How do I use PHPMailer to add a carbon copy recipient?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-add-a-carbon-copy-recipient)