# How do I create and extract a Unix tar file?
// plain

Creating and extracting a Unix tar file is a simple process. To create a tar file, use the command `tar -cvf <name>.tar <files and/or directories>`, where `<name>` is the desired name of the tar file and `<files and/or directories>` is a list of files and/or directories to be included in the tar.

For example, to create a tar file named `my_tar.tar` that includes the file `my_file.txt` and the directory `my_dir`, use the command:
```
tar -cvf my_tar.tar my_file.txt my_dir
```

To extract the contents of a tar file, use the command `tar -xvf <name>.tar`, where `<name>` is the name of the tar file.

For example, to extract the contents of `my_tar.tar`, use the command:
```
tar -xvf my_tar.tar
```

The parts of the command are as follows:
- `tar`: The command to create or extract a tar file.
- `-c`: The flag to create a tar file.
- `-v`: The flag to display the progress of the tar operation.
- `-f`: The flag to specify the name of the tar file.

## Helpful links
- [tar man page](https://linux.die.net/man/1/tar)
- [Creating a Tar File](https://www.cyberciti.biz/faq/howto-create-tar-file-in-linux-unix/)
- [Extracting a Tar File](https://www.cyberciti.biz/faq/howto-extract-tar-file-to-specific-or-different-directory-linux-unix/)

onelinerhub: [How do I create and extract a Unix tar file?](https://onelinerhub.com/cli-tar/how-do-i-create-and-extract-a-unix-tar-file)