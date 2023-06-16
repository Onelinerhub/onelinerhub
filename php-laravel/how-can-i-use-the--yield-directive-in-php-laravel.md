# How can I use the @yield directive in PHP Laravel?
// plain

The @yield directive is used in PHP Laravel to inject content into a layout template. It allows you to define sections of content in a template and then inject those sections into the layout.

For example, the following code block uses the @yield directive to define a section called "title". The content of this section can then be injected into the layout template.

```
@section('title')
    My Page Title
@endsection
```

The content of the section can then be injected into the layout template using the @yield directive.

```
<title>@yield('title')</title>
```

This will output the following:

```
<title>My Page Title</title>
```

The @yield directive can also be used to inject content from a template into a layout template. For example, the following code block defines a template called "content".

```
@section('content')
    <h1>My Page Content</h1>
@endsection
```

The content of this template can then be injected into the layout template using the @yield directive.

```
@yield('content')
```

This will output the following:

```
<h1>My Page Content</h1>
```

The @yield directive is a powerful tool for separating content and layout in PHP Laravel applications.

## Helpful links
- [Laravel Documentation - Blade Templates](https://laravel.com/docs/7.x/blade)
- [Laracasts - Understanding Laravel Blade Template Inheritance](https://laracasts.com/series/laravel-from-scratch-2018/episodes/12)

onelinerhub: [How can I use the @yield directive in PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-use-the--yield-directive-in-php-laravel)