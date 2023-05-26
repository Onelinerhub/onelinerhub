# How to set an HTML body using Swiftmailer?
// plain

Using Swiftmailer, you can set an HTML body for an email message by using the `setBody()` method. This method takes a string argument which should contain the HTML code for the body of the email.

## Example code

```
$message = (new \Swift_Message('My subject'))
  ->setFrom('my@email.com')
  ->setTo('your@email.com')
  ->setBody('<h1>Hello World!</h1>', 'text/html');
```

The code above will create a message with the subject "My subject" from "my@email.com" to "your@email.com" with an HTML body containing the text "Hello World!"

Parts of the code:
- `\Swift_Message('My subject')`: creates a new Swift_Message object with the subject "My subject".
- `setFrom('my@email.com')`: sets the sender of the message to "my@email.com".
- `setTo('your@email.com')`: sets the recipient of the message to "your@email.com".
- `setBody('<h1>Hello World!</h1>', 'text/html')`: sets the body of the message to the HTML code provided, with the content type set to "text/html".

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swift_Message Class Documentation](https://swiftmailer.symfony.com/docs/messages.html)

onelinerhub: [How to set an HTML body using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-an-html-body-using-swiftmailer)