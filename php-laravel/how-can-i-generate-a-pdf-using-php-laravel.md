# How can I generate a PDF using PHP Laravel?
// plain

Generating PDFs using PHP Laravel is a simple process. The following code example shows how to generate a PDF using the Laravel dompdf package.

```
use Dompdf\Dompdf;

$dompdf = new Dompdf();
$dompdf->loadHtml('<h1>Hello world!</h1>');
$dompdf->render();
$dompdf->stream();
```

This code will generate a PDF with the text "Hello world!" in the document.

## Code explanation


1. `use Dompdf\Dompdf;` - This imports the Dompdf package.
2. `$dompdf = new Dompdf();` - This creates a new instance of the Dompdf class.
3. `$dompdf->loadHtml('<h1>Hello world!</h1>');` - This loads the HTML string into the PDF document.
4. `$dompdf->render();` - This renders the PDF document.
5. `$dompdf->stream();` - This streams the PDF document to the browser.

## Helpful links

- [Dompdf Documentation](https://github.com/dompdf/dompdf)
- [Laravel Documentation](https://laravel.com/docs/master/installation)

onelinerhub: [How can I generate a PDF using PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-generate-a-pdf-using-php-laravel)