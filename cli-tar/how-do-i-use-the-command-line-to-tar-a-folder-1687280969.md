# How do I use the command line to tar a folder?
// plain

The command line utility `tar` can be used to create an archive file from a folder. To use `tar` to tar a folder, the command `tar -cvf <archive-name>.tar <directory>` should be used. The `-c` flag tells `tar` to create an archive, the `-v` flag tells `tar` to be verbose and show the progress of the archive creation, and the `-f` flag tells `tar` the name of the archive file to create.

For example, to create an archive of the folder `my-folder` and name it `my-archive.tar`, the following command should be used:

```
tar -cvf my-archive.tar my-folder
```

The output of this command should look something like this:

```
my-folder/
my-folder/file1.txt
my-folder/file2.txt
my-folder/file3.txt
```

The parts of the command are:

- `tar`: The command line utility to create an archive file
- `-c`: The flag to tell `tar` to create an archive
- `-v`: The flag to tell `tar` to be verbose and show the progress of the archive creation
- `-f`: The flag to tell `tar` the name of the archive file to create
- `my-archive.tar`: The name of the archive file to create
- `my-folder`: The directory of the folder to be archived

For more information, see the following links:

- [tar command](https://linux.die.net/man/1/tar)
- [tar command tutorial](https://www.computerhope.com/unix/utar.htm)

onelinerhub: [How do I use the command line to tar a folder?](https://onelinerhub.com/cli-tar/how-do-i-use-the-command-line-to-tar-a-folder-1687280969)