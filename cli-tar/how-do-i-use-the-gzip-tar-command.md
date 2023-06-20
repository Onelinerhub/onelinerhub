# How do I use the gzip tar command?
// plain

The `gzip tar` command is used to compress and archive multiple files and directories into a single file. It is commonly used to reduce the size of a file, and is often used in conjunction with the `tar` command to create a compressed archive.

To use the `gzip tar` command, use the following syntax:

```
tar -czvf <output-filename>.tar.gz <input-files-and-directories>
```

This will create a compressed archive `<output-filename>.tar.gz` containing all of the files and directories specified in `<input-files-and-directories>`.

The following flags are commonly used with the `gzip tar` command:

- `-c`: Create an archive
- `-z`: Compress the archive using gzip
- `-v`: Verbose output
- `-f`: Specify the output filename

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html).

onelinerhub: [How do I use the gzip tar command?](https://onelinerhub.com/cli-tar/how-do-i-use-the-gzip-tar-command)