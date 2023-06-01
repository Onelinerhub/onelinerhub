# How do I set up Amazon PHP hosting?
// plain

Setting up Amazon PHP hosting is a simple process. First, you'll need to sign up for an AWS account. Once you have an account, you can create an Amazon EC2 instance.

Once your EC2 instance is running, you can install the necessary packages for running PHP. For example, you could use the following command to install PHP 7.2 and Apache web server:
```
sudo yum install php72 httpd24
```

You can then configure Apache to serve your PHP files. To do this, you'll need to edit the Apache configuration file (e.g. `/etc/httpd/conf/httpd.conf`) and add the following lines:
```
<FilesMatch \.php$>
    SetHandler application/x-httpd-php
</FilesMatch>
```

Once Apache is configured, you can upload your PHP files to your EC2 instance and they will be served by Apache.

Finally, you'll need to configure your security groups to allow access to the EC2 instance. This can be done in the AWS console.

For more information, see the [Amazon EC2 documentation](https://aws.amazon.com/documentation/ec2/) and the [Apache documentation](https://httpd.apache.org/docs/2.4/).

onelinerhub: [How do I set up Amazon PHP hosting?](https://onelinerhub.com/php-aws/how-do-i-set-up-amazon-php-hosting)