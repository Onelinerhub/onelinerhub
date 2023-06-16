# How do I use PHP Laravel to validate a request?
// plain

Using PHP Laravel to validate a request is a simple process. The first step is to create a validator class. This class will contain the rules that will be used to validate the request.

Next, the validator class should be used in the controller that is handling the request. For example:

```
use App\Http\Requests\MyRequest;

class MyController extends Controller
{
    public function store(MyRequest $request)
    {
        // The request is valid
    }
}
```

The `MyRequest` class should extend the `Illuminate\Foundation\Http\FormRequest` class and should contain the validation rules. For example:

```
namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class MyRequest extends FormRequest
{
    public function rules()
    {
        return [
            'name' => 'required|string|max:255',
            'email' => 'required|email',
        ];
    }
}
```

The `rules()` method should return an array of validation rules. In this example, the `name` field is required and must be a string with a maximum length of 255 characters. The `email` field is also required and must be a valid email address.

If the request fails validation, the controller method will throw a `Illuminate\Validation\ValidationException` and return a response with the validation errors.

## List of code parts with detailed explanation

1. `use App\Http\Requests\MyRequest;` - This line imports the validator class that was created.
2. `class MyController extends Controller` - This line creates the controller class.
3. `public function store(MyRequest $request)` - This line uses the validator class to validate the request.
4. `namespace App\Http\Requests;` - This line creates the validator class.
5. `use Illuminate\Foundation\Http\FormRequest;` - This line imports the `FormRequest` class.
6. `public function rules()` - This method contains the validation rules.
7. `'name' => 'required|string|max:255'` - This line defines the validation rule for the `name` field.

## List of relevant links

- [Laravel Validation Documentation](https://laravel.com/docs/7.x/validation)
- [Form Request Validation Documentation](https://laravel.com/docs/7.x/validation#form-request-validation)

onelinerhub: [How do I use PHP Laravel to validate a request?](https://onelinerhub.com/php-laravel/how-do-i-use-php-laravel-to-validate-a-request)