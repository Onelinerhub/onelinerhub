# How do I use PHPMailer with Yii2?
// plain

Using PHPMailer with Yii2 is a simple process.

First, you need to install the PHPMailer extension for Yii2. This can be done with composer by running the command:

```
composer require "yiisoft/yii2-swiftmailer"
```

Next, you need to configure the application component for PHPMailer in the `config/web.php` file. This should look something like this:

```
'components' => [
    'mailer' => [
        'class' => 'yii\swiftmailer\Mailer',
        'useFileTransport' => false,
        'transport' => [
            'class' => 'Swift_SmtpTransport',
            'host' => 'smtp.example.com',
            'username' => 'username',
            'password' => 'password',
            'port' => '587',
            'encryption' => 'tls',
        ],
    ],
],
```

Finally, you can use PHPMailer in your application by calling the `mailer` component from the application instance. For example:

```
Yii::$app->mailer->compose()
    ->setFrom('from@example.com')
    ->setTo('to@example.com')
    ->setSubject('Message subject')
    ->setTextBody('Plain text content')
    ->send();
```

The above code will send an email from `from@example.com` to `to@example.com` with the subject line `Message subject` and the body `Plain text content`.

## Helpful links

- [Yii2 Documentation - Mailer](https://www.yiiframework.com/doc/guide/2.0/en/tutorial-core-components#mailer)
- [GitHub - yiisoft/yii2-swiftmailer](https://github.com/yiisoft/yii2-swiftmailer)
- [GitHub - PHPMailer/PHPMailer](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I use PHPMailer with Yii2?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-yii-)