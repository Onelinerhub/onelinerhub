# How do I use tar gzip to compress files at a specific level?
// plain

`tar` is a command line tool used to create, modify, and extract archives. `gzip` is a compression algorithm used to compress files. To use `tar` and `gzip` to compress files at a specific level, you can use the following command:

```
tar -zcvf archive-name.tar.gz -C /path/to/files level
```

- `tar`: command to create and modify archives
- `-z`: flag to compress the archive using gzip
- `-c`: flag to create an archive
- `-v`: flag to enable verbose output
- `-f`: flag to specify the name of the archive
- `-C`: flag to specify the directory to archive
- `level`: the compression level (1-9)

This command will create an archive named `archive-name.tar.gz` in the current directory, and compress the files in the `/path/to/files` directory at the specified compression level.

## Helpful links

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_112.html)
- [Gzip Compression](https://www.gzip.org/)

onelinerhub: [How do I use tar gzip to compress files at a specific level?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-gzip-to-compress-files-at-a-specific-level)