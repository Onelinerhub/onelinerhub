# How do I download Laravel using PHP?
// plain

You can download Laravel using PHP by utilizing the Composer Dependency Manager. Composer is a tool for dependency management in PHP. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

To download Laravel using PHP, you need to first install Composer. Here is an example of how to install Composer on Windows:

```
# Download the Windows Installer
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"

# Install Composer
php composer-setup.php

# Remove the Installer
php -r "unlink('composer-setup.php');"
```

Once Composer is installed, you can use it to download Laravel by running the following command in your terminal:

```
composer create-project --prefer-dist laravel/laravel myproject
```

This will download the latest version of Laravel and install it in the `myproject` directory.

## Code explanation


1. `php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"`: This command downloads the Windows Installer from the Composer website.
2. `php composer-setup.php`: This command runs the Windows Installer to install Composer.
3. `php -r "unlink('composer-setup.php');"`: This command removes the Windows Installer after it has been used.
4. `composer create-project --prefer-dist laravel/laravel myproject`: This command downloads the latest version of Laravel and installs it in the `myproject` directory.

## Helpful links

- [Composer](https://getcomposer.org/)
- [Laravel](https://laravel.com/)

onelinerhub: [How do I download Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-download-laravel-using-php)