# How can I generate a PDF from HTML using Laravel and PHP?
// plain

Generating a PDF from HTML using Laravel and PHP is quite simple. You can do this by using the [DomPDF](https://github.com/dompdf/dompdf) library. Here is an example of how to do this:

```php
<?php

// Include autoloader
require_once 'vendor/autoload.php';

// Reference the Dompdf namespace
use Dompdf\Dompdf;

// Instantiate and use the dompdf class
$dompdf = new Dompdf();

// Load HTML content
$dompdf->loadHtml('<h1>Hello world!</h1>');

// (Optional) Setup the paper size and orientation
$dompdf->setPaper('A4', 'landscape');

// Render the HTML as PDF
$dompdf->render();

// Output the generated PDF to Browser
$dompdf->stream();
```

This example will generate a PDF file with the text "Hello world!" displayed in the center of the page.

The code consists of four parts:

1. Including the autoloader: This is necessary to include the DomPDF library.
2. Referencing the Dompdf namespace: This allows us to use the DomPDF classes.
3. Instantiating the dompdf class: This creates an instance of the DomPDF class.
4. Rendering the HTML as PDF: This renders the HTML content as a PDF file.

Finally, the generated PDF is outputted to the browser.

For more information, please refer to the [DomPDF documentation](https://github.com/dompdf/dompdf/blob/develop/doc/domdpf.faq.md).

onelinerhub: [How can I generate a PDF from HTML using Laravel and PHP?](https://onelinerhub.com/php-laravel/how-can-i-generate-a-pdf-from-html-using-laravel-and-php)