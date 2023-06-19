# How to install packages on Amazon EC2 using Yum?
// plain

1. Install Yum on your Amazon EC2 instance by running the following command:
```
sudo yum install yum
```

2. Once Yum is installed, you can use it to install packages on your Amazon EC2 instance. For example, to install the Apache web server, you can run the following command:
```
sudo yum install httpd
```

3. You can also install multiple packages at once. For example, to install Apache and PHP, you can run the following command:
```
sudo yum install httpd php
```

4. You can also specify a particular version of a package to install. For example, to install version 7.3 of PHP, you can run the following command:
```
sudo yum install php73
```

5. You can also use Yum to update existing packages. For example, to update Apache, you can run the following command:
```
sudo yum update httpd
```

6. You can also use Yum to remove packages. For example, to remove Apache, you can run the following command:
```
sudo yum remove httpd
```

7. For more information about using Yum on Amazon EC2, see the [Yum documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-yum.html).

onelinerhub: [How to install packages on Amazon EC2 using Yum?](https://onelinerhub.com/amazon-redshift/how-to-install-packages-on-amazon-ec--using-yum)