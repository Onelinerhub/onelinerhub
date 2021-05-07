# Download remote file from server (using ssh key)

```bash
scp -i ~/.ssh/key user@server.com:/path/to/file /where/to/download
```

- -i ~/.ssh/key - set path to your private key for connection
- user@server.com - remote user and server address
- /path/to/file - path to a file on a remote server
- /where/to/download - local folder to download file from a server to

group: download_file
