# Download and extract tar.gz file

```bash
curl https://examples.onelinerhub.com/file.tar.gz | tar -xz
```

- `curl` - base curl command
- `/file.tar.gz` - tar.gz file URL
- ` | ` - pipe downloaded file content directly to the specified command
- `tar` - tar.gz archive utility
- `-xz` - will extract given archive (passed from downloaded content)

group: download_archive


