# How do I compress a file without using the tar format?
// plain

You can compress a file without using the tar format by using gzip. Gzip is a file format and a software application used for file compression and decompression. To compress a file with gzip, you can use the following command:
```
gzip <filename>
```
This will create a file with the same name as the original file, but with the extension .gz.

To decompress a gzip file, use the following command:
```
gunzip <filename>
```
This will create a file with the same name as the original file, but without the .gz extension.

## Code explanation


- `gzip <filename>`: This command compresses a file using the gzip format.
- `gunzip <filename>`: This command decompresses a gzip file.

## Helpful links

- [Gzip File Compression](https://www.tutorialspoint.com/unix_commands/gzip.htm)
- [Gzip Wikipedia Page](https://en.wikipedia.org/wiki/Gzip)

onelinerhub: [How do I compress a file without using the tar format?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-file-without-using-the-tar-format)