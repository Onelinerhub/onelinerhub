# Replace or add query parameter to the current url

```php
$url = parse_url($_SERVER['REQUEST_URI']);
parse_str($url['query'], $q);
$params = ['a' => 1, 'b' => 2];
foreach ( $params as $k => $v ) $q[$k] = $v;
$new_url = $url['path'] . '?' . http_build_query($q);
```

- parse_url - parse specified url to components
- $_SERVER\['REQUEST_URI'\] - current url
- parse_str - parse query string to key/val array
- $params - list of parameters to add/replace in current query string
- $new_url - will contain updated url
- http_build_query - transform key/val array to query string
