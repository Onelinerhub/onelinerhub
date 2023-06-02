# How do I use PHPMailer with JavaScript?
// plain

PHPMailer is a library for sending emails from PHP. It can also be used with JavaScript, allowing you to send emails from the client side. Here is an example of how to use PHPMailer with JavaScript:

```
// Include the PHPMailer library
const PHPMailer = require('phpmailer');

// Create a new PHPMailer instance
let mail = new PHPMailer();

// Set the sender's address
mail.setFrom('sender@example.com', 'Sender Name');

// Set the recipient's address
mail.addAddress('recipient@example.com', 'Recipient Name');

// Set the subject
mail.Subject = 'Example PHPMailer Message';

// Set the body
mail.Body = 'This is an example message sent using PHPMailer.';

// Send the email
mail.send();
```

This code will send an email from `sender@example.com` to `recipient@example.com` with the subject `Example PHPMailer Message` and body `This is an example message sent using PHPMailer.`.

The code consists of the following parts:

1.  `const PHPMailer = require('phpmailer');` - This line includes the PHPMailer library into the script.
2.  `let mail = new PHPMailer();` - This line creates a new PHPMailer instance.
3.  `mail.setFrom('sender@example.com', 'Sender Name');` - This line sets the sender's address.
4.  `mail.addAddress('recipient@example.com', 'Recipient Name');` - This line sets the recipient's address.
5.  `mail.Subject = 'Example PHPMailer Message';` - This line sets the subject of the email.
6.  `mail.Body = 'This is an example message sent using PHPMailer.';` - This line sets the body of the email.
7.  `mail.send();` - This line sends the email.

For more information on using PHPMailer with JavaScript, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Using-Gmail-with-XOAUTH2).

onelinerhub: [How do I use PHPMailer with JavaScript?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-javascript)