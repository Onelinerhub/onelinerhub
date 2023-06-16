# How do I upload a file using PHP Laravel?
// plain

The following steps explain how to upload a file using PHP Laravel:

1. Create a form in your view file with an input type of file.

```html
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="upload_file" />
    <input type="submit" value="Upload File" />
</form>
```

2. Create a route in your routes file to handle the form submission.

```php
Route::post('/upload', function() {
    // Handle the form submission
});
```

3. Inside the route, you can use the `request()` helper to get the file from the form submission.

```php
$file = request()->file('upload_file');
```

4. Use the `store()` method to store the file in the desired location.

```php
$file->store('uploads');
```

5. You can also use the `storeAs()` method to store the file with a custom name.

```php
$file->storeAs('uploads', 'custom_name.jpg');
```

6. Finally, you can also use the `move()` method to move the file to a different location.

```php
$file->move('/path/to/destination', 'custom_name.jpg');
```

7. You can also use the `validate()` method to validate the uploaded file before storing it.

```php
$this->validate(request(), [
    'upload_file' => 'required|mimes:jpeg,jpg,png|max:2048'
]);
```

## Helpful links

- [Laravel File Uploads](https://laravel.com/docs/7.x/requests#file-uploads)
- [Laravel Validation](https://laravel.com/docs/7.x/validation#rule-mimes)

onelinerhub: [How do I upload a file using PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-upload-a-file-using-php-laravel)