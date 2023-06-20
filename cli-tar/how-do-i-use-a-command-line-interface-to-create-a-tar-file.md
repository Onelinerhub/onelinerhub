# How do I use a command line interface to create a TAR file?
// plain

A command line interface (CLI) can be used to create a TAR file, which is an archive file format that combines multiple files into one file. To create a TAR file, the `tar` command is used. For example, to create a TAR file containing the files `file1.txt` and `file2.txt`, the following command can be used:

```
tar -cf files.tar file1.txt file2.txt
```

The command above will create a TAR file named `files.tar` which contains the two files specified. The parts of the command are as follows:

* `tar` - The command to create a TAR file
* `-cf` - The flags used to indicate the command should create a file
* `files.tar` - The name of the TAR file to be created
* `file1.txt` & `file2.txt` - The files to be included in the TAR file

For more information about the `tar` command please refer to the following links:

* [Linux man page for tar](http://man7.org/linux/man-pages/man1/tar.1.html)
* [GNU tar documentation](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html)

onelinerhub: [How do I use a command line interface to create a TAR file?](https://onelinerhub.com/cli-tar/how-do-i-use-a-command-line-interface-to-create-a-tar-file)