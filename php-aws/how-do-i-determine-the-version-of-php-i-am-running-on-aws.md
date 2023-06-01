# How do I determine the version of PHP I am running on AWS?
// plain

To determine the version of PHP you are running on AWS, you can use the command line.

First, connect to your AWS instance and open the command line.

Once you're in the command line, type in the following command:

```
php -v
```

This should output the version of PHP you are running. For example:

```
PHP 7.2.17 (cli) (built: Apr  2 2019 20:02:20) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
```

The output shows that the version of PHP running on the AWS instance is 7.2.17.

You can also use the `phpinfo()` function to get more detailed information about the version of PHP running on the instance. To use it, create a file called `phpinfo.php` and add the following code to it:

```
<?php
phpinfo();
```

Then, run the file by typing the following command into the command line:

```
php phpinfo.php
```

This should output a detailed page with information about the version of PHP running on the AWS instance.

For more information about how to determine the version of PHP running on your AWS instance, you can check out the [AWS documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-intro.html).

onelinerhub: [How do I determine the version of PHP I am running on AWS?](https://onelinerhub.com/php-aws/how-do-i-determine-the-version-of-php-i-am-running-on-aws)