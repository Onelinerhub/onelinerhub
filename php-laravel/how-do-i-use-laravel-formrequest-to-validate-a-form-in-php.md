# How do I use Laravel FormRequest to validate a form in PHP?
// plain

FormRequest is a powerful feature of Laravel that allows you to validate forms in a clean, concise way. Here's an example of how to use it to validate a form:

```
// Create a Form Request class
use Illuminate\Foundation\Http\FormRequest;

class FormValidationRequest extends FormRequest
{
    public function authorize()
    {
        return true;
    }

    public function rules()
    {
        return [
            'name' => 'required|min:3',
            'email' => 'required|email',
        ];
    }
}

// Create a controller
public function store(FormValidationRequest $request)
{
    // The form has been validated, continue with normal logic
}
```

The code above creates a new FormRequest class called FormValidationRequest. This class contains two methods: `authorize()` and `rules()`. The `authorize()` method returns true or false to indicate whether the user is authorized to make the request. The `rules()` method contains an array of validation rules that will be used to validate the form.

In the controller, you can pass the FormValidationRequest object to the store method, which will automatically validate the form using the rules specified in the FormValidationRequest class. If the validation fails, an exception will be thrown and the user will be redirected back to the form with the errors.

## Helpful links

- [Laravel Documentation - Validation](https://laravel.com/docs/7.x/validation)
- [Laravel Documentation - Form Requests](https://laravel.com/docs/7.x/validation#form-request-validation)

onelinerhub: [How do I use Laravel FormRequest to validate a form in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-formrequest-to-validate-a-form-in-php)