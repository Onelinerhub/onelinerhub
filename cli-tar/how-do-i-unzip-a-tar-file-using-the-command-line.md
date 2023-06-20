# How do I unzip a tar file using the command line?
// plain

Using the command line to unzip a tar file is a fairly straightforward process. The following example code block shows how to unzip a file named `example.tar`:

```
tar -xvf example.tar
```

## Code explanation


* `tar`: the command to run the tar program
* `-x`: the flag to extract the contents of the tar file
* `-v`: the flag to show the progress of the extraction
* `-f`: the flag to specify the name of the tar file

It is also possible to extract the contents of the tar file into a specific directory. To do this, add the `-C` flag followed by the path of the directory. For example:

```
tar -xvf example.tar -C /path/to/directory
```

For more information, please refer to the following links:

* [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
* [How To Extract .Tar.Gz Files using Linux Command Line](https://linuxize.com/post/how-to-extract-tar-gz-files-using-linux-command-line/)

onelinerhub: [How do I unzip a tar file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-unzip-a-tar-file-using-the-command-line)