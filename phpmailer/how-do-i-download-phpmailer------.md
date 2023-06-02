# How do I download PHPMailer 5.2.4?
// plain

1. Download the latest version of PHPMailer from the [GitHub repository](https://github.com/PHPMailer/PHPMailer).
2. Unzip the downloaded file to a folder.
3. Open the file `composer.json` and change the version number to `5.2.4`:
```
"require": {
    "phpmailer/phpmailer": "5.2.4"
}
```
4. Run the command `composer update` in the terminal to download the specified version of PHPMailer.
5. After the installation is complete, the `vendor` folder will contain the PHPMailer files.
6. Include the `autoload.php` file in your project to use PHPMailer:
```php
require 'vendor/autoload.php';
```
7. You can now use the PHPMailer API to send emails.

onelinerhub: [How do I download PHPMailer 5.2.4?](https://onelinerhub.com/phpmailer/how-do-i-download-phpmailer------)