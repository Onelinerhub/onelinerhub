# How do I use the eng.php file with TCPDF?
// plain

The eng.php file is part of the TCPDF library and is used to load language-specific strings for the library. To use it, you need to include it in your PHP code, like this:
```
require_once('tcpdf/config/lang/eng.php');
```
This will load the language strings into the $l array, which you can then use in your code. For example, to get the string for the "OK" button, you can use this code:
```
echo $l['w_ok'];
```
The output of this code would be "OK".

The eng.php file can also be used to set the language of the TCPDF library. To do this, you need to set the global variable $lg before you include the eng.php file. For example, to set the language to Spanish:
```
$lg = 'spa';
require_once('tcpdf/config/lang/eng.php');
```

The parts of the code above are:
- `require_once('tcpdf/config/lang/eng.php');`: This line includes the eng.php file in your code.
- `echo $l['w_ok'];`: This line prints the string for the "OK" button.
- `$lg = 'spa';`: This line sets the language of the TCPDF library to Spanish.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [TCPDF Language Settings](https://tcpdf.org/docs/srcdoc/tcpdf/language-settings.html)

onelinerhub: [How do I use the eng.php file with TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-eng-php-file-with-tcpdf)