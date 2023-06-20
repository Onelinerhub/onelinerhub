# How do I use the Unix tar zip command?
// plain

The Unix `tar` command is used to create, modify, and extract files from an archive file. It is commonly used to compress files into a single archive file, or to extract files from an archive.

The syntax for the `tar` command is as follows:
```
tar [options] [archive file] [files to archive]
```

The `-z` option is used to compress the archive file with gzip.

For example, to create an archive of two files, `file1.txt` and `file2.txt`, and compress it with gzip, the command would be:
```
tar -zcvf archive.tar.gz file1.txt file2.txt
```

The `-c` option tells `tar` to create an archive, the `-v` option tells it to be verbose and display the files that are being archived, and the `-f` option tells `tar` to use the file `archive.tar.gz` as the archive file.

To extract the files from the archive, the command would be:
```
tar -zxvf archive.tar.gz
```

The `-x` option tells `tar` to extract the files from the archive, and the `-v` option tells it to be verbose and display the files that are being extracted.

For more information about the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the Unix tar zip command?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-zip-command)