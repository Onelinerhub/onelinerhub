# How can I use PHP Laravel to resize an image?
// plain

Using PHP Laravel, you can resize an image with the help of the Intervention Image library.

First, you need to install the library by running the following command in the terminal:

```
composer require intervention/image
```

Then, you need to import the library in the controller with the following code:

```
use Intervention\Image\Facades\Image;
```

Next, you can resize the image with the following code:

```
$image = Image::make('public/foo.jpg')->resize(300, 200);
```

Finally, you can save the resized image with the following code:

```
$image->save('public/bar.jpg');
```

## Code explanation


1. `composer require intervention/image` - This command is used to install the Intervention Image library.
2. `use Intervention\Image\Facades\Image;` - This code is used to import the library in the controller.
3. `$image = Image::make('public/foo.jpg')->resize(300, 200);` - This code is used to resize the image.
4. `$image->save('public/bar.jpg');` - This code is used to save the resized image.

## Helpful links

- [Intervention Image Library](http://image.intervention.io/)

onelinerhub: [How can I use PHP Laravel to resize an image?](https://onelinerhub.com/php-laravel/how-can-i-use-php-laravel-to-resize-an-image)