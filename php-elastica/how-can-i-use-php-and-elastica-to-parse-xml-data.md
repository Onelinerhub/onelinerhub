# How can I use PHP and Elastica to parse XML data?
// plain

PHP and Elastica can be used together to parse XML data. This can be done by using the Elastica library in PHP to convert XML data into a PHP array.

## Example code

```php
// Include the Elastica library
require_once '/path/to/elastica/lib/Elastica/Client.php';

// Create a new Elastica Client
$client = new Elastica_Client();

// Create a new XML object
$xml = new Elastica_XML($client);

// Load the XML data
$data = $xml->loadXML('/path/to/xml/data.xml');

// Parse the XML data
$parsed_data = $xml->parseXML($data);
```
## Output example

```
Array
(
    [0] => Array
        (
            [node] => node1
            [value] => value1
        )

    [1] => Array
        (
            [node] => node2
            [value] => value2
        )

)
```

The code above does the following:

1. Includes the Elastica library
2. Creates a new Elastica Client
3. Creates a new XML object
4. Loads the XML data
5. Parses the XML data into a PHP array

For more information, see the [Elastica documentation](https://github.com/ruflin/Elastica).

onelinerhub: [How can I use PHP and Elastica to parse XML data?](https://onelinerhub.com/php-elastica/how-can-i-use-php-and-elastica-to-parse-xml-data)