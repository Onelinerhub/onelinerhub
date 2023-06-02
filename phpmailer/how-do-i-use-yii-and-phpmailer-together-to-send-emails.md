# How do I use Yii and PHPMailer together to send emails?
// plain

Using Yii and PHPMailer together to send emails is a simple process. First, install the PHPMailer library through composer.

```
composer require phpmailer/phpmailer
```

Then, create a new file in the `components` folder of the Yii application. This file should contain a class that extends the `PHPMailer\PHPMailer\PHPMailer` class.

```
<?php

namespace app\components;

use PHPMailer\PHPMailer\PHPMailer;

class Mailer extends PHPMailer
{
    // Mailer class code
}
```

In the class, you can define the settings for the PHPMailer instance, such as the `Host`, `Port`, `Username`, and `Password` for the SMTP server.

```
public function __construct()
{
    parent::__construct();

    $this->Host = 'smtp.example.com';
    $this->Port = 587;
    $this->Username = 'user@example.com';
    $this->Password = 'password';
}
```

Finally, you can use the `Mailer` class to send emails by passing it to the `Yii::$app->mailer` component.

```
$mailer = new Mailer();
Yii::$app->mailer->send($mailer);
```

This will send the email using the settings defined in the `Mailer` class.

## Helpful links
- [Yii Documentation](https://www.yiiframework.com/doc/guide/2.0/en/start-installation)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I use Yii and PHPMailer together to send emails?](https://onelinerhub.com/phpmailer/how-do-i-use-yii-and-phpmailer-together-to-send-emails)