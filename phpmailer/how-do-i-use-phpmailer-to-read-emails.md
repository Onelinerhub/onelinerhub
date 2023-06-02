# How do I use PHPMailer to read emails?
// plain

PHPMailer is a library for sending and receiving emails in PHP. It can be used to read emails using the POP3 protocol. To do this, you need to create a POP3 connection and then get the email messages. Here is an example code block that shows how to do this:

```
// Create a POP3 connection
$pop3 = new POP3();
$pop3->connect('hostname', 110);

// Authenticate
$pop3->login('username', 'password');

// Get the emails
$emails = $pop3->getMessages();
```

This code will create a POP3 connection to a host, authenticate with a username and password, and then get the emails from the server. The `$emails` variable will contain an array of email messages, each of which can be accessed using the `getMessage()` method.

## Code explanation


- `$pop3`: This variable is an instance of the `POP3` class, which is used to create a POP3 connection.
- `connect()`: This method is used to connect to a POP3 server. It takes two parameters: the hostname and the port.
- `login()`: This method is used to authenticate with the POP3 server. It takes two parameters: the username and password.
- `getMessages()`: This method is used to get the emails from the server. It returns an array of email messages.
- `getMessage()`: This method is used to access a single email message. It takes one parameter: the index of the email message in the array.

Here are some ## Helpful links

- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer)
- [POP3 protocol](https://en.wikipedia.org/wiki/Post_Office_Protocol)

onelinerhub: [How do I use PHPMailer to read emails?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-read-emails)