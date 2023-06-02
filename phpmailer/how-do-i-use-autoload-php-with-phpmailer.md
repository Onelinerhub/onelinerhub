# How do I use autoload.php with PHPMailer?
// plain

Using autoload.php with PHPMailer is a great way to quickly include all the necessary files for the library. Autoload.php is a file that is included in the PHPMailer library that allows you to include all the necessary files for the library in one line of code. Here's an example of how to use autoload.php with PHPMailer:

```
require 'PHPMailer/PHPMailerAutoload.php';
```

This code will include all the necessary files for PHPMailer and create a new PHPMailer object. You can then use this object to create and send emails with PHPMailer.

The parts of the code above are as follows:
- `require`: This is the PHP command used to include a file in your code.
- `PHPMailer/PHPMailerAutoload.php`: This is the path to the autoload.php file included with the PHPMailer library.

For more information, see the following links:
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Autoload](https://github.com/PHPMailer/PHPMailer/blob/master/src/PHPMailerAutoload.php)

onelinerhub: [How do I use autoload.php with PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-use-autoload-php-with-phpmailer)