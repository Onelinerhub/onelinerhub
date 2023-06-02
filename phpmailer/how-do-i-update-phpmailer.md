# How do I update PHPMailer?
// plain

Updating PHPMailer is a simple process.

First, you need to download the latest version of PHPMailer from the [official website](https://github.com/PHPMailer/PHPMailer).

Then, you can replace the existing files in your project with the new version.

You can also use composer to update PHPMailer. To do so, add the following code to your composer.json file:

```
"require": {
    "phpmailer/phpmailer": "~6.0"
}
```

Then, run the following command in the terminal to update PHPMailer:

```
composer update
```

The output should be something like this:

```
Loading composer repositories with package information
Updating dependencies (including require-dev)
Package operations: 3 installs, 0 updates, 0 removals
  - Installing psr/log (1.1.3): Loading from cache
  - Installing phpmailer/phpmailer (v6.1.7): Loading from cache
  - Installing league/oauth2-client (2.5.0): Loading from cache
Writing lock file
Generating autoload files
```

After updating, you should check the [official documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial) to make sure you are using the new version correctly.

onelinerhub: [How do I update PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-update-phpmailer)