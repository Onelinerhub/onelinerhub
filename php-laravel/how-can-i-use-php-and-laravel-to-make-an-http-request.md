# How can I use PHP and Laravel to make an HTTP request?
// plain

Using the Laravel HTTP Client, you can make HTTP requests from your PHP code with ease. To use the HTTP Client, you must first import the `Http` facade in your controller:

```php
use Illuminate\Support\Facades\Http;
```

Once imported, you can make a request like this:

```php
$response = Http::get('https://example.com/api/users');
```

The `Http` facade provides a variety of helpful methods for sending HTTP requests. In this example, the `get()` method is used to send a `GET` request to the given URL.

The response will be an instance of `Illuminate\Http\Client\Response`, which provides a variety of methods for inspecting and interacting with the response. For example, you can get the response body using the `body()` method:

```php
$users = $response->body();
```

You can also inspect the status code of the response using the `status()` method:

```php
$statusCode = $response->status();
```

For more information, see the [Laravel HTTP Client documentation](https://laravel.com/docs/master/http-client).

## Helpful links

- [Laravel HTTP Client Documentation](https://laravel.com/docs/master/http-client)

onelinerhub: [How can I use PHP and Laravel to make an HTTP request?](https://onelinerhub.com/php-laravel/how-can-i-use-php-and-laravel-to-make-an-http-request)