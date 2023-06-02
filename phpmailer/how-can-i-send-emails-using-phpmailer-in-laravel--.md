# How can I send emails using PHPMailer in Laravel 8?
// plain

Sending emails using PHPMailer in Laravel 8 is achieved by using the `send` method of the `Mail` facade. This method accepts a `Message` instance, which is created by using the `message` method of the `Mail` facade.

The `message` method accepts a `Closure` that contains the message configuration such as the subject, from address, to address, and the message body.

## Example code

```
Mail::send(
    ['text'=>'mail'],
    $data,
    function($message) use ($data)
    {
       $message->to($data['email'], $data['name'])
               ->subject('Welcome to My Site!');
    }
);
```

The `send` method also accepts a `Mailable` instance, which is created by extending the `Mailable` class. This class contains methods to configure the message such as `from`, `subject`, `view`, `attach`, etc.

## Example code

```
use App\Mail\WelcomeMail;

Mail::to($data['email'], $data['name'])->send(new WelcomeMail());
```

The `send` method returns a `Swift_Message` instance, which is an object representation of the message.

## Helpful links
- [Laravel Mail Documentation](https://laravel.com/docs/8.x/mail)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How can I send emails using PHPMailer in Laravel 8?](https://onelinerhub.com/phpmailer/how-can-i-send-emails-using-phpmailer-in-laravel--)