# How do I extract a file from a Unix tar archive?
// plain

To extract a file from a Unix tar archive, you can use the `tar` command. The basic syntax for extracting a file is `tar -xvf <archive_name.tar> <file_name>`.

For example:
```
tar -xvf myarchive.tar myfile.txt
```
This will extract `myfile.txt` from the `myarchive.tar` archive.

## Code explanation

- `tar`: The tar command used for creating, modifying, and extracting files from archives.
- `-x`: This option tells tar to extract files from an archive.
- `-v`: This option tells tar to display progress information while extracting files.
- `-f`: This option tells tar the name and path of the archive to be extracted.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_51.html)
- [Tar Command Tutorial](https://www.computerhope.com/unix/utar.htm)

onelinerhub: [How do I extract a file from a Unix tar archive?](https://onelinerhub.com/cli-tar/how-do-i-extract-a-file-from-a-unix-tar-archive)