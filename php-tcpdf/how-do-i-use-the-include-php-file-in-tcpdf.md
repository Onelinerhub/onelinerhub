# How do I use the include.php file in TCPDF?
// plain

Include.php is a file in the TCPDF library which allows you to include external PHP files in your PDF document. To use the include.php file in TCPDF, you first need to include the TCPDF library in your project.

```
require_once('tcpdf_include.php');
```

Then you can use the `TCPDF::includeHTML()` method to include external PHP files in your PDF document.

```
$pdf->includeHTML('include.php');
```

The `TCPDF::includeHTML()` method takes two parameters: the path of the external PHP file, and an optional array of parameters.

* `$file`: (string) The path of the external PHP file.
* `$params`: (array) An array of parameters to be passed to the included file.

Here is an example of how to use the `TCPDF::includeHTML()` method with an array of parameters:

```
$params = array('param1' => 'value1', 'param2' => 'value2');
$pdf->includeHTML('include.php', $params);
```

For more information about the `TCPDF::includeHTML()` method, please refer to the official documentation: [TCPDF::includeHTML()](http://www.tcpdf.org/doc/code/classTCPDF.html#a93e2b3a2a06e7a4c3b1c1f2b8b7d8a7a).

onelinerhub: [How do I use the include.php file in TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-include-php-file-in-tcpdf)