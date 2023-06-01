# How do I fix PHP not working on AWS EC2?
// plain

To fix PHP not working on AWS EC2, first check the Apache configuration file. Make sure the following lines are present and not commented out:

```
LoadModule php7_module modules/libphp7.so
AddHandler application/x-httpd-php .php
```

If they are not present, add them to the file and restart Apache.

Next, make sure the correct version of PHP is installed. To check the version, run the following command:

```
php -v
```

The output should look something like this:
```
PHP 7.2.5 (cli) (built: Apr 23 2018 14:50:14) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
```

If the wrong version of PHP is installed, uninstall it and install the correct version.

Finally, check the permissions of the files and directories. Make sure the Apache user has read/write permissions on the files and directories.

If all of the above steps are followed, PHP should work correctly on AWS EC2.

## Code explanation
**
1. LoadModule php7_module modules/libphp7.so
2. AddHandler application/x-httpd-php .php
3. php -v

**## Helpful links**
- [Apache Configuration File](https://httpd.apache.org/docs/2.4/configuring.html)
- [Installing PHP](https://www.php.net/manual/en/install.php)
- [File and Directory Permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html#add-delete-modify-permissions)

onelinerhub: [How do I fix PHP not working on AWS EC2?](https://onelinerhub.com/php-aws/how-do-i-fix-php-not-working-on-aws-ec-)