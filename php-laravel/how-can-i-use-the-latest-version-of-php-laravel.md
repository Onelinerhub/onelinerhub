# How can I use the latest version of PHP Laravel?
// plain

You can use the latest version of PHP Laravel by following these steps:

1. Download the latest version of Composer from [https://getcomposer.org/download/](https://getcomposer.org/download/).

2. Install Composer on your computer.

3. Create a new project using the command `composer create-project --prefer-dist laravel/laravel <project-name>`

This will create a new Laravel project with the latest version of PHP Laravel.

4. Navigate to the project directory and install the dependencies using the command `composer install`.

5. Serve the project using the command `php artisan serve`.

This will start the development server and the project will be available at `http://localhost:8000`.

6. Open the project in your favorite code editor and start coding.

7. Once you are ready to deploy the project, build the project using the command `php artisan build`.

This will create a production-ready version of the project.

## Example code

```
composer create-project --prefer-dist laravel/laravel <project-name>
```

## Output example

```
Crafting application...
Loading composer repositories with package information
Installing dependencies (including require-dev) from lock file
Nothing to install or update
Generating autoload files
> Illuminate\Foundation\ComposerScripts::postAutoloadDump
> @php artisan package:discover
Discovered Package: fideloper/proxy
Discovered Package: laravel/tinker
Package manifest generated successfully.
```

onelinerhub: [How can I use the latest version of PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-use-the-latest-version-of-php-laravel)