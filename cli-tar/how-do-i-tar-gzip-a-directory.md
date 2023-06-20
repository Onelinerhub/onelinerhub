# How do I tar gzip a directory?
// plain

To tar gzip a directory, use the `tar` command with `-z` and `-c` flags.
```
tar -zcvf <name_of_archive>.tar.gz <name_of_directory>
```
This will create a `tar.gz` archive with the contents of the specified directory.

The flags used are:
- `-z`: Compress the resulting archive with gzip.
- `-c`: Create a new archive.
- `-v`: Verbosely list files which are processed.
- `-f`: Specify the filename of the archive.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_49.html)
- [Linux tar command](https://linuxize.com/post/how-to-create-tar-gz-files-in-linux/)

onelinerhub: [How do I tar gzip a directory?](https://onelinerhub.com/cli-tar/how-do-i-tar-gzip-a-directory)