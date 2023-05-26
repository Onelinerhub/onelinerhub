# How to use Swiftmailer with SendGrid?
// plain

Swiftmailer is a popular PHP library for sending emails. It can be used with SendGrid to send emails with ease.

To use Swiftmailer with SendGrid, you need to install the library and configure it with your SendGrid credentials.

## Example code

```
<?php
// Require the Swift Mailer library
require_once 'swift_required.php';

// Your SendGrid credentials
$username = 'YOUR_SENDGRID_USERNAME';
$password = 'YOUR_SENDGRID_PASSWORD';

// Setup Swift mailer parameters
$transport = Swift_SmtpTransport::newInstance('smtp.sendgrid.net', 587);
$transport->setUsername($username);
$transport->setPassword($password);
$swift = Swift_Mailer::newInstance($transport);

// Create a message (subject)
$message = new Swift_Message('Wonderful Subject');

// attach the body of the email
$message->setFrom(array('john@doe.com' => 'John Doe'));
$message->setBody('Here is the message itself');

// send message
if ($recipients = $swift->send($message, $failures))
{
  echo 'Message successfully sent!';
} else {
  echo "There was an error:\n";
  print_r($failures);
}
```

## Output example

```
Message successfully sent!
```

## Code explanation

- Require the Swift Mailer library: This line imports the Swift Mailer library into the script.
- Your SendGrid credentials: This line sets the username and password for your SendGrid account.
- Setup Swift mailer parameters: This line sets up the parameters for the Swift Mailer library, including the SMTP server and port.
- Create a message (subject): This line creates a new Swift_Message object with the subject of the email.
- Attach the body of the email: This line sets the from address and body of the email.
- Send message: This line sends the email using the Swift Mailer library.

## Helpful links
- [Swift Mailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [SendGrid Documentation](https://sendgrid.com/docs/index.html)

onelinerhub: [How to use Swiftmailer with SendGrid?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-with-sendgrid)