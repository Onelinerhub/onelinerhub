# How to parse XML in Twig with PHP?
// plain

Parsing XML in Twig with PHP can be done using the `SimpleXML` extension.

```php
$xml = simplexml_load_string($xml_string);
```

This will create an object of `SimpleXMLElement` class which can be used to access the XML data.

## Code explanation


1. `simplexml_load_string($xml_string)`: This function takes a string containing XML data and returns an object of `SimpleXMLElement` class.

2. `$xml->node`: This is used to access the nodes of the XML data.

## Helpful links

- [SimpleXML](https://www.php.net/manual/en/book.simplexml.php)
- [Twig](https://twig.symfony.com/)

onelinerhub: [How to parse XML in Twig with PHP?](https://onelinerhub.com/twig/how-to-parse-xml-in-twig-with-php-)