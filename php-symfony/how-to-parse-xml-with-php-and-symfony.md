# How to parse XML with PHP and Symfony?
// plain

Parsing XML with PHP and Symfony is a relatively straightforward process. The Symfony framework provides a number of tools to help with this task.

## Example code

```
$xml = simplexml_load_string($xmlString);
$json = json_encode($xml);
$array = json_decode($json, true);
```

## Output example

```
Array
(
    [@attributes] => Array
        (
            [version] => 1.0
            [encoding] => UTF-8
        )

    [node] => Array
        (
            [0] => Array
                (
                    [@attributes] => Array
                        (
                            [name] => Node 1
                        )

                    [value] => Value 1
                )

            [1] => Array
                (
                    [@attributes] => Array
                        (
                            [name] => Node 2
                        )

                    [value] => Value 2
                )

        )

)
```

## Code explanation

1. `simplexml_load_string($xmlString)` - This function takes an XML string and converts it into a SimpleXMLElement object.
2. `json_encode($xml)` - This function takes the SimpleXMLElement object and converts it into a JSON string.
3. `json_decode($json, true)` - This function takes the JSON string and converts it into an associative array.

## Helpful links
- [PHP SimpleXML](https://www.php.net/manual/en/book.simplexml.php)
- [Symfony XML Component](https://symfony.com/doc/current/components/dom_crawler.html)

onelinerhub: [How to parse XML with PHP and Symfony?](https://onelinerhub.com/php-symfony/how-to-parse-xml-with-php-and-symfony)