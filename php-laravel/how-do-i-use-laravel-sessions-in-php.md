# How do I use Laravel sessions in PHP?
// plain

Using sessions in Laravel is very easy and convenient. The following example shows how to use a session in Laravel:

```
// store data in session
$request->session()->put('key', 'value');

// get data from session
$value = $request->session()->get('key');

// remove data from session
$request->session()->forget('key');
```

The first line stores data in the session with the key `key` and the value `value`. The second line retrieves the value stored in the session with the key `key`. The third line removes the data from the session with the key `key`.

You can also store an array of data in the session:

```
// store array of data in session
$request->session()->put(['foo' => 'bar', 'baz' => 'qux']);

// get data from session
$data = $request->session()->all();
```

The first line stores an array of data in the session. The second line retrieves all the data stored in the session.

For more information about using sessions in Laravel, please refer to the official documentation:

- [Session - Laravel](https://laravel.com/docs/7.x/session)

onelinerhub: [How do I use Laravel sessions in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-sessions-in-php)