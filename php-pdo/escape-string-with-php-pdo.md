# Escape string with PHP PDO

```php
$escaped = $pdo->quote("string");
```

- `$escaped =` - will contain escaped string
- `$pdo` - PDO connection object
- `quote` - escapes specified string

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');
echo $pdo->quote("Hi I'm string");
```
```
'Hi I\'m string'
```

