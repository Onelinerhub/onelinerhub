# How to get the message ID in SwiftMailer?
// plain

The message ID in SwiftMailer can be obtained by using the `getId()` method. This method returns a string containing the message ID.

## Example code

```
$messageId = $message->getId();
```

## Output example

```
<20190505095004.1.1557189900@example.com>
```

## Code explanation

- `$message`: An instance of the `Swift_Message` class.
- `getId()`: A method of the `Swift_Message` class which returns the message ID as a string.

## Helpful links
- [SwiftMailer Documentation](https://swiftmailer.symfony.com/docs/messages.html#message-ids)

onelinerhub: [How to get the message ID in SwiftMailer?](https://onelinerhub.com/php-swiftmailer/how-to-get-the-message-id-in-swiftmailer)