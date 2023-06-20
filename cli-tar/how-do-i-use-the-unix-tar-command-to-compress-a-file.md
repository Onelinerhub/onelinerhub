# How do I use the Unix tar command to compress a file?
// plain

The `tar` command is a Unix utility used to create and manipulate tar archives. To compress a file with the `tar` command, use the following syntax:

```
tar -czf <filename>.tar.gz <file_or_directory_to_compress>
```

This command will create a `tar.gz` archive of the specified file or directory.

The parts of the command are:

* `tar`: The command to run
* `-czf`: The flags used to compress and create a new archive
* `<filename>.tar.gz`: The name of the new archive
* `<file_or_directory_to_compress>`: The file or directory to compress

For example, to compress the file `example.txt`, you would run the command:

```
tar -czf example.tar.gz example.txt
```

This will create a `example.tar.gz` archive containing the `example.txt` file.

## Helpful links

* [Tar Command Tutorial](https://www.computerhope.com/unix/utar.htm)
* [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How do I use the Unix tar command to compress a file?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-command-to-compress-a-file)