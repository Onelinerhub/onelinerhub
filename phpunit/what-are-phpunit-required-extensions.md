# What are PHPUnit required extensions
// plain

PHPUnit is a unit testing framework for the PHP programming language. It is an instance of the xUnit architecture for unit testing frameworks.

In order to use PHPUnit, certain extensions must be enabled in the `php.ini` configuration file. These extensions are:

* `extension=php_xsl.dll` - This extension enables the XSLT processor, which is used by PHPUnit to generate reports.

* `extension=php_mbstring.dll` - This extension enables the multibyte string functions, which are used by PHPUnit to process text.

* `extension=php_curl.dll` - This extension enables the cURL library, which is used by PHPUnit to make HTTP requests.

* `extension=php_soap.dll` - This extension enables the SOAP library, which is used by PHPUnit to make SOAP requests.

For more information, please refer to the [PHPUnit documentation](https://phpunit.readthedocs.io/en/latest/).

onelinerhub: [What are PHPUnit required extensions](https://onelinerhub.com/phpunit/what-are-phpunit-required-extensions)