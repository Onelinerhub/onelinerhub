# How do I install PHP on an AWS EC2 instance?
// plain

1. To install PHP on an AWS EC2 instance, you first need to connect to the instance using SSH.
2. Once connected, you can use the following command to install PHP and its dependencies:
    ```
    sudo yum install -y php php-cli php-common php-devel php-mysql
    ```
3. This command will install the latest version of PHP and all the necessary packages.
4. After the installation is complete, you can check the version of PHP installed using the following command:
    ```
    php -v
    ```
    Output:
    ```
    PHP 7.4.7 (cli) (built: Jun  8 2020 11:56:55) ( NTS )
    Copyright (c) The PHP Group
    Zend Engine v3.4.0, Copyright (c) Zend Technologies
    ```
5. To enable PHP on the web server, you can use the following command:
    ```
    sudo service httpd restart
    ```
6. You can now check if PHP is enabled by creating a simple PHP file in the document root of the web server and accessing it with a web browser.
7. For more information, you can refer to the [AWS Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html).

onelinerhub: [How do I install PHP on an AWS EC2 instance?](https://onelinerhub.com/php-aws/how-do-i-install-php-on-an-aws-ec--instance)