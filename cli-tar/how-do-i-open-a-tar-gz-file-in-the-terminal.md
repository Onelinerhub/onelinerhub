# How do I open a tar.gz file in the terminal?
// plain

To open a tar.gz file in the terminal, first you need to unzip the file using the command `tar -xzvf <filename>`. This command will extract the files from the tar.gz archive.

```
tar -xzvf myarchive.tar.gz
x file1.txt
x file2.txt
x file3.txt
```

The `tar` command has several flags:
- `-x` tells tar to extract files from an archive
- `-z` tells tar to decompress the archive using gzip
- `-v` tells tar to list the files it is extracting
- `-f` tells tar the name of the archive file

After the files are extracted, you can access them in the current directory.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html)
- [How to Extract tar.gz Files](https://www.howtogeek.com/248780/how-to-extract-files-from-a-tar-ball-in-linux/)

onelinerhub: [How do I open a tar.gz file in the terminal?](https://onelinerhub.com/cli-tar/how-do-i-open-a-tar-gz-file-in-the-terminal)