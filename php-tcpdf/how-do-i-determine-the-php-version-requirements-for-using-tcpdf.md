# How do I determine the PHP version requirements for using TCPDF?
// plain

To determine the PHP version requirements for using TCPDF, you need to check the [TCPDF documentation](https://tcpdf.org/docs/installation/). According to the documentation, TCPDF requires at least PHP 5.6.0.

You can also check the PHP version requirements using the following code:

```
echo "Current PHP version: " . phpversion();
```

## Output example

```
Current PHP version: 7.2.24
```

The code above prints out the current PHP version. If the version is at least 5.6.0, then TCPDF will work.

onelinerhub: [How do I determine the PHP version requirements for using TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-determine-the-php-version-requirements-for-using-tcpdf)