# How can I update the PHP version on AWS?
// plain

1. Log into the AWS console.
2. Select the EC2 instance you wish to update.
3. Select "Actions" and then "Instance Settings" and then "Change Instance Type".
4. Select the new instance type with the desired PHP version.
5. Select "Apply" to apply the changes.
6. SSH into the instance and run the following command to check the version:
```
$ php -v
```
## Output example

```
PHP 7.2.34 (cli) (built: Apr  8 2020 19:50:20) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
```
7. You can also use the [AWS CLI](https://aws.amazon.com/cli/) to update the PHP version. See the [documentation](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-attribute.html) for more information.

onelinerhub: [How can I update the PHP version on AWS?](https://onelinerhub.com/php-aws/how-can-i-update-the-php-version-on-aws)