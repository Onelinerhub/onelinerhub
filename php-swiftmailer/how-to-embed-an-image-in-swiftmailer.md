# How to embed an image in Swiftmailer?
// plain

To embed an image in Swiftmailer, you need to use the `Embed()` method. This method takes the image file path as an argument and returns a `Swift_Image` object.

## Example code

```
$image = $message->embed(Swift_Image::fromPath('path/to/image.jpg'));
```

## Output example

```
Swift_Image Object
(
    [_name:protected] => Swift_Image
    [_file:protected] => path/to/image.jpg
)
```

## Code explanation

- `$message`: an instance of `Swift_Message` class
- `Embed()`: a method of `Swift_Message` class
- `Swift_Image`: a class
- `fromPath()`: a static method of `Swift_Image` class
- `$image`: a variable to store the `Swift_Image` object

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swift_Message Class](https://swiftmailer.symfony.com/api/master/class-Swift_Message.html)
- [Swift_Image Class](https://swiftmailer.symfony.com/api/master/class-Swift_Image.html)

onelinerhub: [How to embed an image in Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-embed-an-image-in-swiftmailer)