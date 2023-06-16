# How do I use Laravel Valet with PHP?
// plain

Laravel Valet is a development environment for Mac users. It is an easy-to-use development environment for quickly creating and running Laravel applications. It provides a minimalistic development environment that is easy to setup and use. To use Laravel Valet with PHP, you need to install it and configure it first.

1. Install Valet:

```
composer global require laravel/valet
```

2. Configure Valet:

```
valet install
```

3. Create a new directory for your project:

```
mkdir myproject
```

4. Change to the project directory:

```
cd myproject
```

5. Create a new Laravel project:

```
composer create-project laravel/laravel myproject
```

6. Link your project to Valet:

```
valet link
```

7. Access your project in the browser:

```
http://myproject.test
```

Now you can use Laravel Valet with PHP to develop your project.

## Helpful links

- [Laravel Valet Documentation](https://laravel.com/docs/master/valet)
- [Getting Started with Laravel Valet](https://medium.com/@taylorotwell/getting-started-with-laravel-valet-9a8f1a5d5e3e)

onelinerhub: [How do I use Laravel Valet with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-valet-with-php)