# Fix Either should be specified Error in Easy Digital Download (EDD)

```php
add_filter("edd_add_schema_microdata", "__return_false");
```

add this code in function.php current active theme