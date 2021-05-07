# Upload file to a remote server (using ssh key)

```bash
scp -i ~/.ssh/key /path/to/file.txt user@server.com:/path/to/upload
```

- -i ~/.ssh/key - set path to your private key for connection
- /path/to/file.txt - path to local file to upload on a remote server
- user@server.com - remote user and server address
- /path/to/upload - remote folder to upload file to

group: upload_file
