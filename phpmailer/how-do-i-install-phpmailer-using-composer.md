# How do I install PHPMailer using Composer?
// plain

1. Install [Composer](https://getcomposer.org/download/) if you don't have it already.
2. Create a `composer.json` file in your project root directory.
3. Add the following code to the `composer.json` file:
```json
{
    "require": {
        "phpmailer/phpmailer": "^6.0"
    }
}
```
4. Run `composer install` in the command line in the project root directory.
5. This will install PHPMailer into the `vendor` directory.
6. Include the autoloader in your code with the following line:
```php
require 'vendor/autoload.php';
```
7. You can now start using PHPMailer by creating a new `PHPMailer` instance.

**Code parts explanation**

* Line 3: this line tells Composer to install PHPMailer version 6.0 or higher.
* Line 6: this line includes the Composer autoloader which allows us to access the classes from the `vendor` directory.

**Relevant links**

* [PHPMailer installation instructions](https://github.com/PHPMailer/PHPMailer#installation)
* [Composer documentation](https://getcomposer.org/doc/)

onelinerhub: [How do I install PHPMailer using Composer?](https://onelinerhub.com/phpmailer/how-do-i-install-phpmailer-using-composer)