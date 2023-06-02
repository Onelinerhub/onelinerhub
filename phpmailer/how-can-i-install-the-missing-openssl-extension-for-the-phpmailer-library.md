# How can I install the missing openssl extension for the PHPMailer library?
// plain

1. Download the latest version of the openssl extension for your version of PHP from the [PHP downloads page](https://www.php.net/downloads).
2. Unzip the downloaded file and copy the `php_openssl.dll` file into your `php/ext` directory.
3. Open your `php.ini` file and add the following line to the extensions section:
```
extension=php_openssl.dll
```
4. Restart your web server.
5. Verify that the extension is enabled by running the following code:
```
<?php
if (extension_loaded('openssl')) {
    echo 'Openssl extension is enabled';
}
```
## Output example
 `Openssl extension is enabled`
6. Finally, make sure that the PHP Mailer library is configured to use the openssl extension by setting the `SMTPSecure` option to `ssl` or `tls` in your code.
7. You can now use the PHPMailer library to send emails securely using the openssl extension.

onelinerhub: [How can I install the missing openssl extension for the PHPMailer library?](https://onelinerhub.com/phpmailer/how-can-i-install-the-missing-openssl-extension-for-the-phpmailer-library)