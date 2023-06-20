# file

How do I compress a non tar file using gzip?
// plain

You can compress a non tar file using gzip by using the command `gzip <filename>` in the terminal. This command will create a compressed version of the file with the same name but with the .gz extension. For example, if you have a file named `myfile.txt`, running `gzip myfile.txt` will create a compressed file named `myfile.txt.gz`.

```
$ gzip myfile.txt
$ ls
myfile.txt  myfile.txt.gz
```

The command `gzip` has several options that can be used to customize the compression process. For example, the `-k` option can be used to keep the original file after compression.

```
$ gzip -k myfile.txt
$ ls
myfile.txt  myfile.txt.gz
```

To decompress a gzip file, you can use the command `gunzip <filename>`. For example, to decompress `myfile.txt.gz` you can run `gunzip myfile.txt.gz`.

```
$ gunzip myfile.txt.gz
$ ls
myfile.txt
```

## Code explanation

- `gzip <filename>`: compresses the given file and creates a compressed version with the same name and a .gz extension
- `-k` option: keeps the original file after compression
- `gunzip <filename>`: decompresses the given file

## Helpful links
- [gzip man page](https://linux.die.net/man/1/gzip)
- [gunzip man page](https://linux.die.net/man/1/gunzip)

onelinerhub: [file

How do I compress a non tar file using gzip?](https://onelinerhub.com/cli-tar/file--how-do-i-compress-a-non-tar-file-using-gzip)