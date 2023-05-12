# How to output XML from MySQL using PHP?
// plain

To output XML from MySQL using PHP, the following steps can be taken:

1. Connect to the MySQL database using `mysqli_connect()` function.

```php
$conn = mysqli_connect("localhost", "username", "password", "database");
```

2. Execute a query to retrieve the data from the database using `mysqli_query()` function.

```php
$result = mysqli_query($conn, "SELECT * FROM table");
```

3. Create an XML document using `DOMDocument` class.

```php
$doc = new DOMDocument();
```

4. Create a root element and append it to the document using `createElement()` and `appendChild()` methods.

```php
$root = $doc->createElement("root");
$doc->appendChild($root);
```

5. Iterate through the result set and create child elements for each row using `createElement()` and `appendChild()` methods.

```php
while ($row = mysqli_fetch_assoc($result)) {
    $node = $doc->createElement("node");
    $node->appendChild($doc->createElement("id", $row['id']));
    $node->appendChild($doc->createElement("name", $row['name']));
    $root->appendChild($node);
}
```

6. Output the XML document using `saveXML()` method.

```php
echo $doc->saveXML();
```

## Output example

```xml
<?xml version="1.0"?>
<root>
  <node>
    <id>1</id>
    <name>John</name>
  </node>
  <node>
    <id>2</id>
    <name>Jane</name>
  </node>
</root>
```

## Helpful links

- [PHP: mysqli_connect - Manual](https://www.php.net/manual/en/function.mysqli-connect.php)
- [PHP: mysqli_query - Manual](https://www.php.net/manual/en/function.mysqli-query.php)
- [PHP: DOMDocument - Manual](https://www.php.net/manual/en/class.domdocument.php)
- [PHP: mysqli_fetch_assoc - Manual](https://www.php.net/manual/en/function.mysqli-fetch-assoc.php)

onelinerhub: [How to output XML from MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-output-xml-from-mysql-using-php)