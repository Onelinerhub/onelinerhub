# How can I resolve the "PHPMailer not found" error?
// plain

The "PHPMailer not found" error is a common issue when working with the PHPMailer library. To resolve this error, you need to first make sure that the PHPMailer library is installed and included in your project.

If the library is not installed, you can install it using Composer by running the following command:

```
composer require phpmailer/phpmailer
```

Once the library is installed, you need to include it in your project. This can be done by adding the following line of code at the beginning of your script:

```
require 'vendor/autoload.php';
```

This will include all the necessary files from the PHPMailer library and should resolve the "PHPMailer not found" error.

## Code explanation

1. `composer require phpmailer/phpmailer`: This command is used to install the PHPMailer library using Composer.
2. `require 'vendor/autoload.php';`: This line of code is used to include the PHPMailer library in the project.

## Helpful links
- [PHPMailer Installation Guide](https://github.com/PHPMailer/PHPMailer/blob/master/docs/INSTALL.md)
- [Using Composer](https://getcomposer.org/doc/01-basic-usage.md)

onelinerhub: [How can I resolve the "PHPMailer not found" error?](https://onelinerhub.com/phpmailer/how-can-i-resolve-the--phpmailer-not-found--error)