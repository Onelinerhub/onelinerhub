# How do I tar a folder and its subfolders in Unix?
// plain

The tar command is used to create an archive file of a directory and its subdirectories in Unix. To tar a folder and its subfolders, use the following command:

```
tar -cvf <name-of-archive-file>.tar <name-of-directory>
```

For example, to create an archive file called "my-archive.tar" of the folder "my-folder", use the following command:

```
tar -cvf my-archive.tar my-folder
```

This command will create a tar file of the folder and its subfolders. The c option stands for create, v stands for verbose, and f stands for file.

The following command can be used to extract the files from the tar archive:

```
tar -xvf <name-of-archive-file>.tar
```

For example, to extract the files from the "my-archive.tar" file, use the following command:

```
tar -xvf my-archive.tar
```

The x option stands for extract, v stands for verbose, and f stands for file.

## Code explanation
**

- `tar`: the command used to create an archive file of a directory and its subdirectories
- `-cvf`: the options used to create the archive file (create, verbose, file)
- `-xvf`: the options used to extract the files from the archive (extract, verbose, file)

**## Helpful links**

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linux Tar Command Tutorial](https://linuxize.com/post/how-to-use-tar-command-in-linux/)

onelinerhub: [How do I tar a folder and its subfolders in Unix?](https://onelinerhub.com/cli-tar/how-do-i-tar-a-folder-and-its-subfolders-in-unix)