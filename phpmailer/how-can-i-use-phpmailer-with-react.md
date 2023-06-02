# How can I use PHPMailer with React?
// plain

PHPMailer is a popular email sending library for PHP which can also be used with React. It is very easy to get started with PHPMailer. Here is an example code block to use PHPMailer with React:

```
import PHPMailer from 'phpmailer/phpmailer';

const mailer = new PHPMailer();

// Configure mailer
mailer.Host = 'smtp.example.com';
mailer.Port = 587;
mailer.Username = 'username@example.com';
mailer.Password = 'password';
mailer.SMTPAuth = true;

// Set message
mailer.setFrom('username@example.com', 'Example User');
mailer.addAddress('recipient@example.com', 'Recipient User');
mailer.Subject = 'Test Email';
mailer.Body = 'This is a test email.';

// Send message
mailer.send((error, result) => {
  if (error) {
    console.log(error);
  } else {
    console.log(result);
  }
});
```

The example code above configures the PHPMailer instance with the SMTP server details and sets the message details. Then it sends the message and handles the response.

## Code explanation


1. Import PHPMailer: `import PHPMailer from 'phpmailer/phpmailer';`
2. Create PHPMailer instance: `const mailer = new PHPMailer();`
3. Configure mailer: `mailer.Host`, `mailer.Port`, `mailer.Username`, `mailer.Password`, `mailer.SMTPAuth`
4. Set message: `mailer.setFrom()`, `mailer.addAddress()`, `mailer.Subject`, `mailer.Body`
5. Send message: `mailer.send()`

## Helpful links

- [PHPMailer official documentation](https://github.com/PHPMailer/PHPMailer)
- [How to send email using PHPMailer and React](https://www.tutorialspoint.com/how-to-send-email-using-phpmailer-and-react)

onelinerhub: [How can I use PHPMailer with React?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-react)