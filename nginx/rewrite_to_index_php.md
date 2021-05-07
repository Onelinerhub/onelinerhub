# Rewrite everything to index.php

```nginx
location / {
  try_files $uri /index.php?$args;
}
```

- /index.php?$args - all requests for missing files will be sent to index.php including arguments
