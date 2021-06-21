# CORS rule to allow all origins to access page

```php
if ( isset($_SERVER['HTTP_ORIGIN']) ) {
  header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
  header('Access-Control-Allow-Credentials: true');
}
```

- $_SERVER\['HTTP_ORIGIN'\] - contains origin URL that requested our page
- Access-Control-Allow-Origin - allow access to the origin passed (thus, all origins will be allowed)
- Access-Control-Allow-Credentials - also enabling cookies and auth headers sharing
