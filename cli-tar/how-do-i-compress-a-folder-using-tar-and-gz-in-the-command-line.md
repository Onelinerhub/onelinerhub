# How do I compress a folder using tar and gz in the command line?
// plain

The `tar` command can be used to compress a folder in the command line. The `gz` option is used to compress the folder with the `gzip` algorithm.

To compress a folder using `tar` and `gz`, use the following command:
```
tar -czvf <output-filename>.tar.gz <input-folder>
```
The flags used in this command are:
- `-c`: create a new archive
- `-z`: compress the archive with `gzip`
- `-v`: verbose mode - show the progress while creating the archive
- `-f`: specify the filename of the archive

The output of this command will be a single `tar.gz` file containing the compressed folder.

## Helpful links
- [tar command reference](https://www.computerhope.com/unix/utar.htm)
- [gzip command reference](https://www.computerhope.com/unix/ugzip.htm)

onelinerhub: [How do I compress a folder using tar and gz in the command line?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-folder-using-tar-and-gz-in-the-command-line)