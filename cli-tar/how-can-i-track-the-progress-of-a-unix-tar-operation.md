# How can I track the progress of a Unix tar operation?
// plain

To track the progress of a Unix tar operation, you can use the `--totals` flag in the `tar` command. This flag will print out the total number of files and the total number of bytes written to the archive.

For example:
```
$ tar --totals -cf archive.tar /path/to/files
Total bytes written: 2097152 (2.0MiB, 2.1MB)
Total number of files: 3
```

The command consists of the following parts:

* `tar`: the command that creates the archive
* `--totals`: the flag that prints out the progress information
* `-cf`: the flags that indicate to `tar` to create a file archive
* `archive.tar`: the file name of the archive
* `/path/to/files`: the directory containing the files to archive

For more information, see [GNU tar Manual](https://www.gnu.org/software/tar/manual/html_node/Totals.html).

onelinerhub: [How can I track the progress of a Unix tar operation?](https://onelinerhub.com/cli-tar/how-can-i-track-the-progress-of-a-unix-tar-operation)