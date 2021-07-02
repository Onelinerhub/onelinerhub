# Upload a file

```bash
curl -F file=@file.txt https://example.org/script.php
```

- -F - uploads specified file as multipart form post
- file= - variable name (on the server) to upload file to
- file.txt - path to local file that we want to upload
- example.org/script.php - example script to upload file to

group: upload
