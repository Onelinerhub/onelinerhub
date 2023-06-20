# How do I create a tarball using the command line?
// plain

Creating a tarball using the command line is a simple task. To do this, you will need to use the `tar` command. The basic syntax for creating a tarball is as follows:

```
tar -cvf <tarball_name>.tar <files_to_archive>
```

The parts of this command are as follows:
* `tar`: the command itself
* `-c`: create a new tarball
* `-v`: verbosely show the progress of the tarball creation
* `-f`: the name of the tarball to be created
* `<tarball_name>.tar`: the name of the tarball to be created
* `<files_to_archive>`: the files and/or directories to be archived

For example, if you wanted to create a tarball called `my_archive.tar` containing the files `file1.txt` and `file2.txt`, you would run the following command:

```
tar -cvf my_archive.tar file1.txt file2.txt
```

This would create a tarball called `my_archive.tar` containing the two files.

## Helpful links
* [tar command man page](https://linux.die.net/man/1/tar)
* [Linux tar command tutorial](https://www.linux.com/training-tutorials/how-use-tar-command-linux/)

onelinerhub: [How do I create a tarball using the command line?](https://onelinerhub.com/cli-tar/how-do-i-create-a-tarball-using-the-command-line)