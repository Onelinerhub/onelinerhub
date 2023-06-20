# How do I use the Unix tar syntax?
// plain

The `tar` command is a Unix utility that is used to archive multiple files into a single file. The syntax for using the `tar` command is as follows:

```
tar -[options] [filename.tar] [files]
```

where:

* `-options`: Options that control how the archive is created.
* `filename.tar`: The name of the archive file to be created.
* `files`: The files to be archived.

For example, to create an archive file of the files `file1.txt` and `file2.txt` and name the archive `myarchive.tar`, the command would be:

```
tar -cvf myarchive.tar file1.txt file2.txt
```

In this example, the options used are:

* `-c`: Create an archive.
* `-v`: Verbose output.
* `-f`: Specify the name of the archive file.

The output of this command would be:

```
file1.txt
file2.txt
```

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html).

onelinerhub: [How do I use the Unix tar syntax?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-syntax)