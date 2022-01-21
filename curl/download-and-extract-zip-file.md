# Download and extract zip file

```bash
curl https://examples.onelinerhub.com/file.zip -o /tmp/tmp.zip && unzip /tmp/tmp.zip && rm /tmp/tmp.zip
```

- `curl` - base curl command
- `/file.zip` - zip file URL
- `-o` - specify file name to save downloaded file to
- `/tmp/tmp.zip` - temporary name for a zip file to save to
- `unzip` - will extract specified zip file (`/tmp/tmp.zip` in our case)
- `rm` - remove specified file (`/tmp/tmp.zip` in our case)

group: download_archive


