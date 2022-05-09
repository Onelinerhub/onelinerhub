# Show progress bar for file uploads

```bash
curl -o /tmp/u.tmp -# https://example.org/ -F 'file=@file.txt' && cat /tmp/u.tmp && rm /tmp/u.tmp
```

- `-o /tmp/u.tmp` - redirect output to tmp file
- `-#` - enabled progress bar
- `example.org` - URL to upload file to
- `-F 'file=@file.txt'` - select [file to upload](/curl/upload_file)
- `cat /tmp/u.tmp` - print output
- `rm /tmp/u.tmp` - rm temporary output file


link_youtube: https://youtu.be/pHFMan-FNbA
