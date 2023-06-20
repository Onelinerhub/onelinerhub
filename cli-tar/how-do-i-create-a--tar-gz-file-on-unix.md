# How do I create a .tar.gz file on Unix?
// plain

Creating a .tar.gz file on Unix can be done using the tar command.

```
tar -czvf <filename>.tar.gz <directory>
```

This command will create a .tar.gz file containing the contents of the specified directory.

- `tar`: The command used to create a .tar.gz file
- `-c`: The flag used to create a new archive
- `-z`: The flag used to compress the archive with gzip
- `-v`: The flag used to verbosely list the files being archived
- `-f`: The flag used to specify the filename of the archive
- `<filename>`: The filename of the archive
- `<directory>`: The directory to be archived

For example, to create a .tar.gz file of the `example` directory, the command would be:

```
tar -czvf example.tar.gz example
```

This will create a .tar.gz file called `example.tar.gz` containing the contents of the `example` directory.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_51.html)
- [How to Create and Extract tar.gz Files in Linux](https://www.howtogeek.com/248780/how-to-create-and-extract-tar-gz-files-in-linux/)

onelinerhub: [How do I create a .tar.gz file on Unix?](https://onelinerhub.com/cli-tar/how-do-i-create-a--tar-gz-file-on-unix)