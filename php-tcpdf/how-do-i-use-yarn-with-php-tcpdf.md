# How do I use Yarn with PHP TCPDF?
// plain

Using [Yarn](https://yarnpkg.com/) with [PHP TCPDF](https://tcpdf.org/) is a convenient way to manage dependencies and packages. The following steps will help you get started:

1. Install Yarn:

```
$ npm install -g yarn
```

2. Install the PHP TCPDF package:

```
$ yarn add tcpdf
```

3. Create a `composer.json` file in the root of your project and add the following:

```json
{
    "require": {
        "tcpdf/tcpdf": "^6.2"
    }
}
```

4. Install the package with Yarn:

```
$ yarn install
```

5. Create a `index.php` file in the root of your project and add the following:

```php
<?php

require_once 'vendor/autoload.php';

$pdf = new TCPDF();

$pdf->AddPage();

$pdf->Write(0, 'Hello World!');

$pdf->Output('example.pdf', 'I');
```

6. Run the script:

```
$ php index.php
```

7. Open the generated PDF file:

```
$ open example.pdf
```

The generated PDF should contain the text `Hello World!`

## Helpful links

- [Yarn Documentation](https://yarnpkg.com/en/docs)
- [TCPDF Documentation](https://tcpdf.org/docs.php)

onelinerhub: [How do I use Yarn with PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-use-yarn-with-php-tcpdf)