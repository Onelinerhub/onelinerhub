# How do I tar a file using the command line?
// plain

To tar a file using the command line, you can use the `tar` command. The syntax is as follows:

```
tar -cvf <filename>.tar <filename>
```

This will create a tar file called `<filename>.tar` containing the file `<filename>`. For example, to tar the file `example.txt`:

```
tar -cvf example.tar example.txt
```

This will create a tar file called `example.tar` containing the file `example.txt`.

The parts of the command are as follows:

* `tar`: the tar command
* `-cvf`: the flags for creating a tar file
    * `-c`: create a tar file
    * `-v`: verbose output
    * `-f`: specify the filename of the tar file
* `<filename>.tar`: the name of the tar file to be created
* `<filename>`: the name of the file to be tarred

For more information about the `tar` command, see the [GNU tar man page](https://www.gnu.org/software/tar/manual/html_node/tar_6.html).

onelinerhub: [How do I tar a file using the command line?](https://onelinerhub.com/cli-tar/how-do-i-tar-a-file-using-the-command-line)