# How do I use tar and gzip to password protect a file?
// plain

Using tar and gzip to password protect a file is a two-step process. First, the file needs to be compressed and then encrypted.

1. Compress the file with gzip:
```
gzip -c <filename> > <filename>.gz
```

2. Encrypt the compressed file with tar:
```
tar -czf - <filename>.gz | openssl des3 -salt -k <password> > <filename>.tar.gz
```

- `gzip -c <filename> > <filename>.gz`: This command compresses the file with gzip and creates a `.gz` file.
- `tar -czf - <filename>.gz`: This command combines the compressed file with tar and creates a `.tar.gz` file.
- `openssl des3 -salt -k <password>`: This command encrypts the file with a password.

The resulting file will be `<filename>.tar.gz` and it will be password protected.

## Helpful links
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)
- [Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [OpenSSL Manual](https://www.openssl.org/docs/manmaster/man1/openssl.html)

onelinerhub: [How do I use tar and gzip to password protect a file?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-and-gzip-to-password-protect-a-file)