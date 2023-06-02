# How do I check which version of PHPMailer I'm using?
// plain

To check which version of PHPMailer you are using, you can use the `getVersion()` method. This method will return the version of PHPMailer you are currently using.

## Example code


```
<?php
require 'PHPMailerAutoload.php';
$mail = new PHPMailer;
echo $mail->getVersion();
?>
```

## Output example


```
6.1.7
```

The code above will output the version of PHPMailer you are currently using. The `require` statement is used to include the `PHPMailerAutoload.php` file, which contains the `PHPMailer` class. The `PHPMailer` class is then instantiated to create an object, `$mail`. Finally, the `getVersion()` method is called on the `$mail` object to retrieve the version of PHPMailer.

For more information on the `getVersion()` method, you can visit the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/PHPMailer.md#getversion).

onelinerhub: [How do I check which version of PHPMailer I'm using?](https://onelinerhub.com/phpmailer/how-do-i-check-which-version-of-phpmailer-i-m-using)