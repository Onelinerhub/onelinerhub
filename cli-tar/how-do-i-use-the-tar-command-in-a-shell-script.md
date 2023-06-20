# How do I use the tar command in a shell script?
// plain

The `tar` command is a useful tool for creating and manipulating archives of files in the Linux/Unix shell. It can be used in a shell script to quickly and easily create archives, extract files, and perform other tasks related to archiving.

Here is an example of a shell script that uses the `tar` command to create an archive of a directory:

```
#!/bin/bash

# Create an archive of the directory
tar -cvf my_archive.tar my_directory

# List the contents of the archive
tar -tvf my_archive.tar
```

The output of this script would look something like this:

```
-rw-r--r-- user/user 0 2020-07-20 18:20 my_directory/file1.txt
-rw-r--r-- user/user 0 2020-07-20 18:21 my_directory/file2.txt
```

The script uses the following options:

* `-c`: Create an archive
* `-v`: Verbose output (list the contents of the archive)
* `-f`: Specify the filename of the archive

For more information on the `tar` command and its various options, please refer to the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the tar command in a shell script?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-in-a-shell-script)