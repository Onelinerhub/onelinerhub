# How do I create a login page using PHP and Laravel?
// plain

Creating a login page using PHP and Laravel is quite easy.

First, create a `routes/web.php` file and add the following code to it:

```
Route::get('login', 'Auth\LoginController@showLoginForm')->name('login');
Route::post('login', 'Auth\LoginController@login');
Route::post('logout', 'Auth\LoginController@logout')->name('logout');
```

This will create the routes for the login page.

Next, create a `resources/views/auth/login.blade.php` file and add the following code to it:

```
<form method="POST" action="{{ route('login') }}">
    @csrf

    <div>
        <label for="email">{{ __('E-Mail Address') }}</label>
        <input id="email" type="email" name="email" value="{{ old('email') }}" required autocomplete="email" autofocus>
    </div>

    <div>
        <label for="password">{{ __('Password') }}</label>
        <input id="password" type="password" name="password" required autocomplete="current-password">
    </div>

    <div>
        <input type="checkbox" name="remember" id="remember" {{ old('remember') ? 'checked' : '' }}>
        <label for="remember">
            {{ __('Remember Me') }}
        </label>
    </div>

    <div>
        <button type="submit">
            {{ __('Login') }}
        </button>

        @if (Route::has('password.request'))
            <a href="{{ route('password.request') }}">
                {{ __('Forgot Your Password?') }}
            </a>
        @endif
    </div>
</form>
```

This will create the form for the login page.

Finally, create a `controllers/Auth/LoginController.php` file and add the following code to it:

```
<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\AuthenticatesUsers;

class LoginController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Login Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles authenticating users for the application and
    | redirecting them to your home screen. The controller uses a trait
    | to conveniently provide its functionality to your applications.
    |
    */

    use AuthenticatesUsers;

    /**
     * Where to redirect users after login.
     *
     * @var string
     */
    protected $redirectTo = '/home';

    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest')->except('logout');
    }
}
```

This will handle the authentication of the user.

Now you have a login page using PHP and Laravel.

## Helpful links

* [Laravel Authentication Documentation](https://laravel.com/docs/master/authentication)
* [Laravel Routing Documentation](https://laravel.com/docs/master/routing)
* [Laravel Views Documentation](https://laravel.com/docs/master/views)

onelinerhub: [How do I create a login page using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-do-i-create-a-login-page-using-php-and-laravel)