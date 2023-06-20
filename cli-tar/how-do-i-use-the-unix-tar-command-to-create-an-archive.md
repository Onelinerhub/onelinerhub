# How do I use the Unix tar command to create an archive?
// plain

The `tar` command is a widely used Unix command that allows you to create an archive of files. To use `tar` to create an archive, you will need to specify the `-cvf` flags and the name of the archive file you wish to create.

For example, to create an archive named `my_archive.tar` of the files `file1.txt` and `file2.txt` in the current directory, you can use the following command:

```
tar -cvf my_archive.tar file1.txt file2.txt
```

This will create an archive named `my_archive.tar` in the current directory containing the two files `file1.txt` and `file2.txt`.

The `-cvf` flags are used as follows:

* `-c`: This flag tells `tar` to create an archive.
* `-v`: This flag tells `tar` to output a verbose list of the files it is archiving.
* `-f`: This flag tells `tar` to use the following argument as the name of the archive file.

You can also use `tar` to add files to an existing archive. To do this, you will need to use the `-rvf` flags instead of `-cvf`.

For example, to add the file `file3.txt` to the existing archive `my_archive.tar`, you can use the following command:

```
tar -rvf my_archive.tar file3.txt
```

This will add the file `file3.txt` to the existing archive `my_archive.tar`.

You can find more detailed information about the `tar` command and its flags [here](https://linuxize.com/post/how-to-use-tar-command-in-linux/).

onelinerhub: [How do I use the Unix tar command to create an archive?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-command-to-create-an-archive)