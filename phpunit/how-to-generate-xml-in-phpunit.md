# How to generate XML in PHPUnit?
// plain

XML can be generated in PHPUnit using the `assertXmlStringEqualsXmlString()` assertion. This assertion compares two given XML strings and returns true if they are equal.

## Example

```
$xml1 = '<foo><bar>baz</bar></foo>';
$xml2 = '<foo><bar>baz</bar></foo>';

$this->assertXmlStringEqualsXmlString($xml1, $xml2);
```

## Output example

```
OK (1 test, 1 assertion)
```

## Code explanation

- `assertXmlStringEqualsXmlString()`: assertion to compare two given XML strings
- `$xml1`: first XML string to compare
- `$xml2`: second XML string to compare

Explanation:
The `assertXmlStringEqualsXmlString()` assertion compares two given XML strings and returns true if they are equal. In the example, `$xml1` and `$xml2` are equal, so the assertion returns true and the test passes.

## Helpful links
- [PHPUnit Documentation - Assertions](https://phpunit.readthedocs.io/en/9.2/assertions.html)

onelinerhub: [How to generate XML in PHPUnit?](https://onelinerhub.com/phpunit/how-to-generate-xml-in-phpunit)