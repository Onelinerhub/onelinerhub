# How to add an attachment from a string using Swiftmailer?
// plain

Using Swiftmailer, you can add an attachment from a string by creating a `Swift_Attachment` object and passing the string as the first parameter. The second parameter is the filename of the attachment.

## Example code

```
$attachment = Swift_Attachment::newInstance($string, 'filename.txt');
```

The code above will create a new attachment object with the string as the content and the filename as the second parameter.

## Code explanation

- `Swift_Attachment::newInstance()`: creates a new attachment object
- `$string`: the string to be attached
- `'filename.txt'`: the filename of the attachment

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to add an attachment from a string using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-add-an-attachment-from-a-string-using-swiftmailer)