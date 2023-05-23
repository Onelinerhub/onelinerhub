# How to create a progress bar with PHP Symfony?
// plain

Creating a progress bar with PHP Symfony is easy.

First, you need to create a `ProgressBar` object with the total number of steps:

```php
$progressBar = new ProgressBar(100);
```

Then, you can start the progress bar and advance it with the `advance()` method:

```php
$progressBar->start();

for ($i = 0; $i < 100; $i++) {
    // Do something
    $progressBar->advance();
}
```

The `ProgressBar` class also provides methods to set the current step, the message, the format, and the bar width.

- `setStep($step)`: Sets the current step.
- `setMessage($message)`: Sets the message to be displayed.
- `setFormat($format)`: Sets the format of the progress bar.
- `setBarWidth($width)`: Sets the width of the progress bar.

For more information, please refer to the [official documentation](https://symfony.com/doc/current/components/console/helpers/progressbar.html).

onelinerhub: [How to create a progress bar with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-create-a-progress-bar-with-php-symfony)