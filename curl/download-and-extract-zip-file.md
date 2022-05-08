# Download and extract zip file

### This will extract downloaded zip archive into current directory:

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


link_youtube: https://youtu.be/yAe69Fv499g
