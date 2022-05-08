# Download and extract gzip file

```bash
curl https://examples.onelinerhub.com/file.yml.gz | gzip -d > file.yml
```

- `curl` - base curl command
- `/file.yml.gz` - gzip file URL
- ` | ` - pipe downloaded file content directly to the specified command
- `gzip -d` - decompress given gzip archive
- `>` - saves output to the specified file
- `file.yml` - name of the file to write decompressed contents into

group: download_archive


link_youtube: https://youtu.be/6yHuFcQhIXs
