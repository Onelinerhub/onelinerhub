# How do I convert a gzip file to a tar file?
// plain

Converting a gzip file to a tar file is a two-step process. First, you need to decompress the gzip file using the `gunzip` command. Then, you can use the `tar` command to create a tar file from the decompressed gzip file.

## Example


```
gunzip my_file.gz
tar -cvf my_file.tar my_file
```

The `gunzip` command decompresses the gzip file and stores it in the same directory as the original file. The `tar` command creates a tar file from the decompressed gzip file.

## Code explanation

- `gunzip`: decompresses the gzip file
- `tar -cvf`: creates a tar file

## Helpful links
- [How to Convert a GZIP File to a Tar File](https://www.howtogeek.com/361481/how-to-convert-a-gzip-file-to-a-tar-file/)
- [gunzip command](https://linux.die.net/man/1/gunzip)
- [tar command](https://linux.die.net/man/1/tar)

onelinerhub: [How do I convert a gzip file to a tar file?](https://onelinerhub.com/cli-tar/how-do-i-convert-a-gzip-file-to-a-tar-file)