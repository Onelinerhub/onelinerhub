# How do I open a tar.gz file using the command line?
// plain

The `tar.gz` file format is a combination of two different technologies, `tar` and `gzip`. `tar` is a program used to store multiple files in a single file, while `gzip` is a program used to compress files.

To open a `tar.gz` file using the command line, you can use the following command:

```
tar -xvzf <filename>.tar.gz
```

This command will extract the files within the `tar.gz` archive.

The command consists of four parts:

* `tar`: The program used to extract the files from the archive
* `-x`: Tells `tar` to extract the files
* `-v`: Tells `tar` to display a verbose output
* `-z`: Tells `tar` to unzip the archive
* `-f`: Tells `tar` which file to extract

For more information, you can refer to the following links:

* [How to Extract tar.gz Files](https://www.linux.com/tutorials/how-extract-tar-gz-files-linux/)
* [tar command in Linux with Examples](https://www.geeksforgeeks.org/tar-command-in-linux-with-examples/)

onelinerhub: [How do I open a tar.gz file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-open-a-tar-gz-file-using-the-command-line)