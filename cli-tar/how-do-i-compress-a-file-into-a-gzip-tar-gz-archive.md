# How do I compress a file into a GZIP tar.gz archive?
// plain

1. Create a tar archive of the file or folder you want to compress:
```
tar -zcvf archive.tar.gz /path/to/file_or_folder
```

2. This command creates a tar archive named `archive.tar.gz` in the current directory. The `-z` flag indicates that the archive should be compressed with gzip. The `-c` flag indicates that the archive should be created, and the `-v` flag indicates that the progress should be verbosely listed to the console.

3. You can also use the `-f` flag to specify the name of the archive:
```
tar -zcvf my_archive.tar.gz /path/to/file_or_folder
```

4. To extract the contents of a gzip tar archive, use the `-x` flag instead of the `-c` flag:
```
tar -zxvf archive.tar.gz
```

5. This command extracts the contents of `archive.tar.gz` to the current directory.

6. You can also use the `--list` flag to view the contents of the archive without extracting it:
```
tar -ztvf archive.tar.gz
```

7. This command lists the contents of `archive.tar.gz` to the console.

## Code explanation
**
- `-z`: compress the archive with gzip
- `-c`: create a new archive
- `-v`: verbosely list the progress to the console
- `-f`: specify the name of the archive
- `-x`: extract the contents of the archive
- `--list`: list the contents of the archive without extracting it

**## Helpful links**
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html)
- [Linux Tar Command Tutorial](https://www.computerhope.com/unix/utar.htm)

onelinerhub: [How do I compress a file into a GZIP tar.gz archive?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-file-into-a-gzip-tar-gz-archive)