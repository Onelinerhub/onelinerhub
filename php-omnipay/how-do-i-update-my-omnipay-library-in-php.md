# How do I update my Omnipay library in PHP?
// plain

Updating the Omnipay library in PHP is relatively easy and requires minimal effort. First, you need to install the library using composer:

```
composer require omnipay/omnipay
```

Once the library is installed, you can update it to the latest version using the following command:

```
composer update omnipay/omnipay
```

The output of the command should look something like this:

```
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 1 install, 0 updates, 0 removals
  - Installing omnipay/omnipay (v3.3.1): Downloading (100%)
Writing lock file
Generating autoload files
```

You can also specify a specific version of the library to update to by using the `--with-dependencies` flag:

```
composer update omnipay/omnipay --with-dependencies
```

This will update the library to the version specified in the `composer.json` file.

You can also use the `--prefer-stable` flag to ensure that the latest stable version of the library is installed:

```
composer update omnipay/omnipay --prefer-stable
```

## Helpful links

- [Composer Documentation](https://getcomposer.org/doc/)
- [Omnipay Documentation](https://omnipay.thephpleague.com/docs/)

onelinerhub: [How do I update my Omnipay library in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-update-my-omnipay-library-in-php)