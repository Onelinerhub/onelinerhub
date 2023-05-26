# How to add an attachment using Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in PHP. To add an attachment using Swiftmailer, you need to use the `addAttachment()` method.

## Example code

```
$message = (new Swift_Message('Hello World'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself')
  ->addAttachment(Swift_Attachment::fromPath('/path/to/file.pdf'));
```

The `addAttachment()` method takes a `Swift_Attachment` object as an argument. The `Swift_Attachment` class provides several methods to create an attachment, such as `fromPath()` which takes the path to the file as an argument.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swift_Attachment Class Documentation](https://swiftmailer.symfony.com/docs/messages.html#attachments)

onelinerhub: [How to add an attachment using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-add-an-attachment-using-swiftmailer)