# How do I use PHPMailer to create a form?
// plain

PHPMailer is a powerful library for sending emails using PHP. To create a form with PHPMailer, you need to first create an HTML form with the necessary form fields. Then, you need to create a PHP script to handle the form submission and send the email. The following example code block will demonstrate how to do this:

```
// Create the HTML form
<form method="post" action="send_email.php">
  <input type="text" name="name" placeholder="Name">
  <input type="text" name="email" placeholder="Email">
  <textarea name="message" placeholder="Message"></textarea>
  <button type="submit">Send Email</button>
</form>

// Create the PHP script
<?php
  // Import PHPMailer classes into the global namespace
  use PHPMailer\PHPMailer\PHPMailer;
  use PHPMailer\PHPMailer\Exception;

  // Load Composer's autoloader
  require 'vendor/autoload.php';

  // Get form data
  $name = $_POST['name'];
  $email = $_POST['email'];
  $message = $_POST['message'];

  // Instantiate a new PHPMailer
  $mail = new PHPMailer(true);

  // Set the sender and recipient
  $mail->setFrom($email, $name);
  $mail->addAddress('recipient@example.com');

  // Set the email body
  $mail->Subject = 'New Message';
  $mail->Body = $message;

  // Send the email
  $mail->send();
?>
```

The code above will create an HTML form with three fields (name, email and message) and a submit button. On submission, the form data will be sent to the `send_email.php` script which will use PHPMailer to send an email with the message to the recipient.

## Code explanation

1. HTML form - creates the form with the necessary fields
2. `use` statements - imports the PHPMailer classes into the global namespace
3. `require` statement - loads the Composer autoloader
4. `$_POST` variables - gets the form data
5. `new PHPMailer` - instantiates a new PHPMailer
6. `setFrom` and `addAddress` - sets the sender and recipient
7. `Subject` and `Body` - sets the email body
8. `send` - sends the email

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [HTML Forms Tutorial](https://www.w3schools.com/html/html_forms.asp)

onelinerhub: [How do I use PHPMailer to create a form?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-create-a-form)