# How can I resolve a "PHP Omnipay Not Found" error?
// plain

PHP Omnipay Not Found error usually occurs when you try to use the Omnipay library but the library is not installed. To resolve this error, you need to install the library first.

To install Omnipay, you can use Composer. For example, you can use the following command in terminal:

```
composer require league/omnipay
```

This will install the library and resolve the error.

If you are using a framework, you may need to make some additional changes to make sure the library is loaded correctly. For example, if you are using Laravel, you need to add the following line in `config/app.php`:

```
'Omnipay\Omnipay' => 'Omnipay\OmnipayServiceProvider',
```

After that, you need to run the following command to clear the configuration cache:

```
php artisan config:cache
```

This should resolve the PHP Omnipay Not Found error.

## Helpful links
- [Composer Documentation](https://getcomposer.org/doc/)
- [Omnipay Documentation](https://omnipay.thephpleague.com/getting-started/)
- [Laravel Documentation](https://laravel.com/docs/7.x/configuration#environment-configuration)

onelinerhub: [How can I resolve a "PHP Omnipay Not Found" error?](https://onelinerhub.com/php-omnipay/how-can-i-resolve-a--php-omnipay-not-found--error)