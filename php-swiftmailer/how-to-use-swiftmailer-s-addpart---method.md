# How to use Swiftmailer's addPart() method?
// plain

The `addPart()` method of Swiftmailer is used to add a part to a message. It takes two parameters: the body of the message and the content type.

## Example

```
$message->addPart('This is the body of the message', 'text/plain');
```

The code above will add a plain text part to the message.

Parts of the code:
- `$message`: an instance of the `Swift_Message` class
- `addPart()`: the method used to add a part to the message
- `'This is the body of the message'`: the body of the message
- `'text/plain'`: the content type of the message

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to use Swiftmailer's addPart() method?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-s-addpart---method)