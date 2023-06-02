# How do I use the PHP TCPDF namespace?
// plain

TCPDF is a PHP library used to generate PDF documents. The TCPDF namespace is used to access the classes and functions of the TCPDF library.

To use the TCPDF namespace, you must first include the library in your PHP script. This can be done using the `require_once` function:

```php
require_once('tcpdf/tcpdf.php');
```

After including the library, you can access the classes and functions of the TCPDF namespace by prefixing them with `TCPDF::`. For example, you can create a new instance of the TCPDF class using the `new` keyword:

```php
$pdf = new TCPDF();
```

You can also access the functions and constants of the TCPDF namespace without the `TCPDF::` prefix, as they are defined in the global scope. For example, you can set the page orientation using the `setPageOrientation` function:

```php
$pdf->setPageOrientation('P', true, 0);
```

You can also access the constants of the TCPDF namespace, such as `K_PATH_MAIN`:

```php
echo TCPDF_STATIC::K_PATH_MAIN; // Outputs: /home/user/tcpdf/
```

For more information, please see the [TCPDF documentation](https://tcpdf.org/docs/).

onelinerhub: [How do I use the PHP TCPDF namespace?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-php-tcpdf-namespace)