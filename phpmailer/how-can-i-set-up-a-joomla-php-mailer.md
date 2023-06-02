# How can I set up a Joomla PHP mailer?
// plain

Setting up a Joomla PHP mailer requires several steps. First, you need to create a `mailer.php` file and place it in the `/libraries/joomla/mail/` folder. This file should contain the following code:

```php
<?php
defined('_JEXEC') or die;

jimport('joomla.mail.mail');

class JMailWrapper extends JMail
{
    public static function sendMail($from, $fromName, $recipient, $subject, $body, $mode=0, $cc=null, $bcc=null, $attachment=null, $replyTo=null, $replyToName=null)
    {
        $mail = new JMailWrapper();
        $mail->setSender(array($from, $fromName));
        $mail->addRecipient($recipient);
        $mail->setSubject($subject);
        $mail->setBody($body);
        if ($mode) {
            $mail->isHTML(true);
        }
        if ($cc) {
            $mail->addCC($cc);
        }
        if ($bcc) {
            $mail->addBCC($bcc);
        }
        if ($attachment) {
            $mail->addAttachment($attachment);
        }
        if ($replyTo) {
            $mail->addReplyTo($replyTo, $replyToName);
        }
        $send = $mail->Send();
        if ($send !== true) {
            echo 'Error sending email: ' . $send->__toString();
        } else {
            echo 'Email sent successfully!';
        }
    }
}
```

Then, you need to create a `configuration.php` file in the `/libraries/joomla/mail/` folder and add the following code:

```php
<?php
defined('_JEXEC') or die;

$mailer = JMailWrapper::getMailer();
$mailer->IsSMTP();
$mailer->Host = 'smtp.example.com';
$mailer->SMTPAuth = true;
$mailer->Username = 'username';
$mailer->Password = 'password';
$mailer->SMTPSecure = 'tls';
$mailer->Port = 587;
```

Finally, you need to call the `sendMail()` method in the `mailer.php` file with the appropriate parameters. For example:

```php
JMailWrapper::sendMail('sender@example.com', 'Sender Name', 'recipient@example.com', 'Test Email', 'This is a test email.');
```

## Output example
 `Email sent successfully!`

## Code explanation


- `mailer.php`: This file contains the `JMailWrapper` class which is used to send emails. It contains the `sendMail()` method which takes several parameters such as the sender, recipient, subject, and body of the email.
- `configuration.php`: This file contains the configuration for the mailer. It sets the SMTP host, username, password, etc.
- `JMailWrapper::sendMail()`: This method is used to send emails. It takes several parameters such as the sender, recipient, subject, and body of the email.

## Helpful links

- [Joomla Mailer Documentation](https://docs.joomla.org/Sending_email_from_extensions)
- [JMailWrapper Class Documentation](https://api.joomla.org/cms-3/classes/JMailWrapper.html)

onelinerhub: [How can I set up a Joomla PHP mailer?](https://onelinerhub.com/phpmailer/how-can-i-set-up-a-joomla-php-mailer)