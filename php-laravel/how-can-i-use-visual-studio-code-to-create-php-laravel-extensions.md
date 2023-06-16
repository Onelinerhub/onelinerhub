# How can I use Visual Studio Code to create PHP Laravel extensions?
// plain

Visual Studio Code (VSC) is an open source code editor that can be used to create PHP Laravel extensions. To get started, you need to install the Laravel Extension Pack, which includes a set of extensions to help you develop Laravel applications. To install the pack, open up VSC and click on the Extensions tab. Then, search for “Laravel Extension Pack” and click install.

Once the pack is installed, you can start creating your own Laravel extensions. To do this, you need to create a folder in your project directory and add a file called `extension.php`. This file will contain your extension code.

For example, you could create a simple extension to add a custom route to your application. To do this, you would add the following code to the `extension.php` file:

```
<?php

Route::get('/custom-route', function () {
    return 'This is a custom route';
});
```

If you run your application, you will see the custom route you created.

To learn more about creating Laravel extensions with VSC, you can check out the official [Laravel documentation](https://laravel.com/docs/7.x/extending). Additionally, there are a number of tutorials available online, such as [this one](https://code.tutsplus.com/tutorials/how-to-create-laravel-extensions-with-visual-studio-code--cms-31967) from TutsPlus.

onelinerhub: [How can I use Visual Studio Code to create PHP Laravel extensions?](https://onelinerhub.com/php-laravel/how-can-i-use-visual-studio-code-to-create-php-laravel-extensions)