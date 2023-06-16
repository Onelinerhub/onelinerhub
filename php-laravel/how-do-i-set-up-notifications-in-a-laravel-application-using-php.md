# How do I set up notifications in a Laravel application using PHP?
// plain

In order to set up notifications in a Laravel application using PHP, you will need to first install the laravel/ui package with the following command:
```
composer require laravel/ui
```

In order to use notifications, you will need to configure the notification class. To do this, open the `AppServiceProvider.php` file and add the following code to the `boot` method:
```
use Illuminate\Notifications\Notification;

Notification::routes();
```

To create a notification class, use the following Artisan command:
```
php artisan make:notification NewNotification
```

This will create a new notification class in the `app/Notifications` directory. You can then add any logic to the `toMail` method. For example:
```
public function toMail($notifiable)
{
    return (new MailMessage)
                ->line('The introduction to the notification.')
                ->action('Notification Action', url('/'))
                ->line('Thank you for using our application!');
}
```

To send the notification, use the `notify` method in your controller or model. For example:
```
$user->notify(new NewNotification);
```

Finally, you can view the notifications in the `database/migrations/notifications` table.

## Helpful links

- [Notification Documentation](https://laravel.com/docs/7.x/notifications)
- [Laravel UI Package](https://laravel.com/docs/7.x/frontend)

onelinerhub: [How do I set up notifications in a Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-do-i-set-up-notifications-in-a-laravel-application-using-php)