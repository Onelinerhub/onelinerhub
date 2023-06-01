# How do I install PHP extensions on Amazon's Elastic Beanstalk?
// plain

1. To install PHP extensions on Amazon's Elastic Beanstalk, you need to add the extension to the `.ebextensions` folder in the root of your application source bundle.
2. Create a file named `01_install_php_extension.config` in the `.ebextensions` folder and add the following code block to it:
```
packages:
  yum:
    php-<extension-name>: []
```
The code block above will install the PHP extension specified by `<extension-name>`.
3. Upload the application source bundle to the Elastic Beanstalk environment.
4. After the new version of the application is deployed, SSH into the EC2 instance and run the following command to verify the installation:
```
$ php -m | grep <extension-name>
```
If the extension is installed correctly, it should be listed in the output of the command.
5. To enable the extension, open the `php.ini` file located in `/etc/php.d/` and add the following line:
```
extension=<extension-name>.so
```
6. Restart the web server for the changes to take effect:
```
$ sudo /etc/init.d/httpd restart
```
7. Verify the installation again by running the command from step 4.

## Helpful links
- [Installing PHP Extensions on Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-extensions.html)

onelinerhub: [How do I install PHP extensions on Amazon's Elastic Beanstalk?](https://onelinerhub.com/php-elastica/how-do-i-install-php-extensions-on-amazon-s-elastic-beanstalk)