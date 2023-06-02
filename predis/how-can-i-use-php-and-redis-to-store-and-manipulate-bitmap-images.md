# How can I use PHP and Redis to store and manipulate bitmap images?
// plain

Using PHP and Redis, bitmap images can be stored and manipulated in a variety of ways. PHP can be used to read in the image file and then convert it into a binary string. Redis can then be used to store the binary string in a key-value pair.

## Example code

```php
$imageFile = file_get_contents('image.bmp');
$binaryString = bin2hex($imageFile);
$redis->set('image', $binaryString);
```

The binary string can then be retrieved from Redis and used to manipulate the image. For example, the image can be resized using PHP's `imagecopyresampled` function.

## Example code

```php
$binaryString = $redis->get('image');
$imageFile = hex2bin($binaryString);
$image = imagecreatefromstring($imageFile);
$resizedImage = imagecreatetruecolor(100, 100);
imagecopyresampled($resizedImage, $image, 0, 0, 0, 0, 100, 100, imagesx($image), imagesy($image));
header('Content-Type: image/bmp');
imagebmp($resizedImage);
```

## Output example
 Resized image in BMP format.

## Code explanation

- `file_get_contents('image.bmp')`: reads the image file into a string.
- `bin2hex($imageFile)`: converts the image file string into a binary string.
- `$redis->set('image', $binaryString)`: stores the binary string in a key-value pair in Redis.
- `$binaryString = $redis->get('image')`: retrieves the binary string from Redis.
- `hex2bin($binaryString)`: converts the binary string back into a string.
- `imagecreatefromstring($imageFile)`: creates an image resource from the string.
- `imagecopyresampled($resizedImage, $image, 0, 0, 0, 0, 100, 100, imagesx($image), imagesy($image))`: resizes the image.
- `header('Content-Type: image/bmp')`: sets the content type of the response.
- `imagebmp($resizedImage)`: outputs the resized image in BMP format.

## Helpful links
- [PHP file_get_contents](https://www.php.net/manual/en/function.file-get-contents.php)
- [PHP bin2hex](https://www.php.net/manual/en/function.bin2hex.php)
- [PHP hex2bin](https://www.php.net/manual/en/function.hex2bin.php)
- [PHP imagecreatefromstring](https://www.php.net/manual/en/function.imagecreatefromstring.php)
- [PHP imagecopyresampled](https://www.php.net/manual/en/function.imagecopyresampled.php)
- [PHP header](https://www.php.net/manual/en/function.header.php)
- [PHP imagebmp](https://www.php.net/manual/en/function.imagebmp.php)

onelinerhub: [How can I use PHP and Redis to store and manipulate bitmap images?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-store-and-manipulate-bitmap-images)