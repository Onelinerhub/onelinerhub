# How do I extract a tar.bz2 file using the command line?
// plain

To extract a tar.bz2 file using the command line, use the following command:

```
tar -xvjf <file_name>.tar.bz2
```

This will extract the contents of the tar.bz2 file into the current directory.

The parts of this command are as follows:

* `tar`: The tar command is used to create, manipulate, and extract files that are archived in the tar format.
* `-x`: This flag tells tar to extract the contents of the file.
* `-v`: This flag tells tar to be verbose and display the progress of the extraction.
* `-j`: This flag tells tar to use bzip2 for compression.
* `-f`: This flag tells tar to use the file specified after it.

For more information on the tar command, see the following link:

* [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How do I extract a tar.bz2 file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-extract-a-tar-bz--file-using-the-command-line)