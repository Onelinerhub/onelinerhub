# How to use Bootstrap with PHP Symfony?
// plain

Bootstrap is a popular front-end framework for developing responsive, mobile-first web applications. It can be used with PHP Symfony to create modern, responsive web applications.

To use Bootstrap with PHP Symfony, you need to install the Bootstrap bundle. This bundle provides integration with the Bootstrap framework.

```
composer require mopa/bootstrap-bundle
```

The output of the above command should be something like this:

```
Using version ^4.0 for mopa/bootstrap-bundle
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 1 install, 0 updates, 0 removals
  - Installing mopa/bootstrap-bundle (v4.0.0): Downloading (100%)
Writing lock file
Generating autoload files
```

Once the bundle is installed, you can use the Bootstrap classes in your Symfony templates. For example, to create a Bootstrap alert, you can use the following code:

```
<div class="alert alert-success" role="alert">
  This is a success alert—check it out!
</div>
```

The above code will create a Bootstrap alert with a success message.

## Helpful links

- [Mopa Bootstrap Bundle](https://github.com/phiamo/MopaBootstrapBundle)
- [Bootstrap Documentation](https://getbootstrap.com/docs/4.3/getting-started/introduction/)

onelinerhub: [How to use Bootstrap with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-bootstrap-with-php-symfony)