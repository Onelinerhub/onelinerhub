# How do I choose between PHP TCPDF and mPDF for software development?
// plain

Choosing between PHP TCPDF and mPDF for software development depends on the project requirements.

For example, if the project requires a large number of complex documents to be generated, then TCPDF may be a better choice due to its advanced features. However, if the project is focused on generating simpler documents, then mPDF may be a better choice due to its simplicity of use.

Below is an example of a simple PDF document generated using mPDF:

```
<?php
require_once __DIR__ . '/vendor/autoload.php';

$mpdf = new \Mpdf\Mpdf();
$mpdf->WriteHTML('<h1>Hello world!</h1>');
$mpdf->Output();
```

The output of this code is the PDF document containing the text "Hello world!".

When deciding between PHP TCPDF and mPDF, the following should be taken into consideration:

* Ease of use - mPDF has a simpler learning curve and is easier to use than TCPDF
* Features - TCPDF has more advanced features than mPDF
* Performance - mPDF has better performance than TCPDF

## Helpful links

* [mPDF Documentation](https://mpdf.github.io/)
* [TCPDF Documentation](http://www.tcpdf.org/docs.php)

onelinerhub: [How do I choose between PHP TCPDF and mPDF for software development?](https://onelinerhub.com/php-tcpdf/how-do-i-choose-between-php-tcpdf-and-mpdf-for-software-development)