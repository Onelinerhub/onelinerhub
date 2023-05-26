# How to send multiple attachments with SwiftMailer?
// plain

SwiftMailer can be used to send multiple attachments with a single email. To do this, you need to create a `Swift_Attachment` object for each attachment and add it to the `Swift_Message` object.

## Example code

```php
<?php
// Create the message
$message = new Swift_Message();

// Create the attachment
$attachment1 = Swift_Attachment::fromPath('/path/to/file1.pdf');
$attachment2 = Swift_Attachment::fromPath('/path/to/file2.pdf');

// Add the attachments to the message
$message->attach($attachment1);
$message->attach($attachment2);

// Send the message
$mailer->send($message);
```

## Output example

```
Message sent successfully
```

## Code explanation


1. `$message = new Swift_Message();` - This creates a new `Swift_Message` object which will be used to send the email.

2. `$attachment1 = Swift_Attachment::fromPath('/path/to/file1.pdf');` - This creates a new `Swift_Attachment` object from the specified file path.

3. `$message->attach($attachment1);` - This adds the attachment to the message.

4. `$mailer->send($message);` - This sends the message with the attachments.

## Helpful links

- [SwiftMailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to send multiple attachments with SwiftMailer?](https://onelinerhub.com/php-swiftmailer/how-to-send-multiple-attachments-with-swiftmailer)