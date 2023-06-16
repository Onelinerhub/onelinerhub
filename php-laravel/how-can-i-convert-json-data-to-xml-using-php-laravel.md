# How can I convert JSON data to XML using PHP Laravel?
// plain

To convert JSON data to XML using PHP Laravel, you can use the `json_encode()` and `simplexml_load_string()` functions.

## Example code

```
$json = '{"name": "John", "age": 30, "city": "New York"}';
$json_array = json_decode($json, true); // convert JSON to array
$xml = simplexml_load_string("<root></root>"); // create a new XML element
array_walk_recursive($json_array, array ($xml, 'addChild')); // add array elements to XML
print $xml->asXML(); // output XML
```
## Output example

```
<?xml version="1.0"?>
<root>
  <name>John</name>
  <age>30</age>
  <city>New York</city>
</root>
```

## Code explanation

- `json_decode()`: converts a JSON string to a PHP array
- `simplexml_load_string()`: creates a new SimpleXMLElement object from a given string
- `array_walk_recursive()`: iterates over each element of an array and applies a user-defined function to each element
- `addChild()`: adds an element to the SimpleXMLElement object
- `asXML()`: outputs the XML in a string

## Helpful links
- [PHP json_encode()](https://www.php.net/manual/en/function.json-encode.php)
- [PHP simplexml_load_string()](https://www.php.net/manual/en/function.simplexml-load-string.php)
- [PHP array_walk_recursive()](https://www.php.net/manual/en/function.array-walk-recursive.php)
- [PHP SimpleXMLElement addChild()](https://www.php.net/manual/en/simplexmlelement.addchild.php)
- [PHP SimpleXMLElement asXML()](https://www.php.net/manual/en/simplexmlelement.asxml.php)

onelinerhub: [How can I convert JSON data to XML using PHP Laravel?](https://onelinerhub.com/php-laravel/how-can-i-convert-json-data-to-xml-using-php-laravel)