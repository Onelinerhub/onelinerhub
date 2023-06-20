# How do I use the gzip tar command in Linux?
// plain

The `gzip tar` command is used to create a compressed archive file in Linux. It combines the `gzip` and `tar` commands to compress and combine multiple files into one archive file.

## Example


```
tar -czf archive.tar.gz file1 file2 file3
```

This command will combine `file1`, `file2`, and `file3` into a single `archive.tar.gz` file.

Parts of the command:

- `tar`: the tar command is used to create an archive
- `-czf`: the `-c` flag creates an archive, the `-z` flag compresses the archive using `gzip`, and the `-f` flag specifies the filename of the archive
- `archive.tar.gz`: the name of the archive that will be created
- `file1 file2 file3`: the files to be combined into the archive

For more information, see the following links:

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_119.html)
- [Linux Gzip Command Tutorial](https://www.geeksforgeeks.org/gzip-command-in-linux-with-examples/)

onelinerhub: [How do I use the gzip tar command in Linux?](https://onelinerhub.com/cli-tar/how-do-i-use-the-gzip-tar-command-in-linux)