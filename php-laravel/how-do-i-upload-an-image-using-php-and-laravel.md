# How do I upload an image using PHP and Laravel?
// plain

To upload an image using PHP and Laravel, you need to follow the steps below:

1. Create a form in your Laravel view file with an input type of file:
```
<form action="{{ route('image.upload') }}" method="POST" enctype="multipart/form-data">
    <input type="file" name="image">
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

2. Create a route to handle the form submission in your routes/web.php file. The route should point to a controller function that will handle the upload:
```
Route::post('/image/upload', 'ImageController@upload')->name('image.upload');
```

3. Create a controller to handle the form submission. The controller function should validate the image and then store it to the public/images folder:
```
public function upload(Request $request)
{
    $this->validate($request, [
        'image' => 'required|image|mimes:jpeg,png,jpg,gif,svg|max:2048',
    ]);

    $imageName = time().'.'.$request->image->getClientOriginalExtension();
    $request->image->move(public_path('images'), $imageName);
    return back()
        ->with('success','Image Uploaded successfully.')
        ->with('path',$imageName);
}
```

4. Finally, you can access the uploaded image in your view file using the path stored in the session:
```
@if (session()->has('path'))
    <img src="{{ asset('images/' . session()->get('path')) }}" alt="">
@endif
```

## Helpful links
- [Laravel File Upload Tutorial](https://itsolutionstuff.com/post/laravel-56-image-upload-tutorialexample.html)
- [Laravel Validation](https://laravel.com/docs/5.6/validation)
- [Laravel Request](https://laravel.com/docs/5.6/requests)

onelinerhub: [How do I upload an image using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-do-i-upload-an-image-using-php-and-laravel)