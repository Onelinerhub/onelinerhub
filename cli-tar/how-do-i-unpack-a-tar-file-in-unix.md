# How do I unpack a tar file in Unix?
// plain

In order to unpack a tar file in Unix, you can use the `tar` command. The command has the following syntax:

```
tar -xvf file.tar
```

The `-x` flag tells tar to extract the files, the `-v` flag tells tar to list the files as it unpacks them, and the `-f` flag tells tar which file to unpack.

The command will produce output similar to the following:

```
x file1
x file2
x file3
```

The output will list each file as it is unpacked.

## Code explanation

- `tar`: the command used to unpack the tar file
- `-x`: tells tar to extract the files
- `-v`: tells tar to list the files as they are unpacked
- `-f`: tells tar which file to unpack

## Helpful links
- [Tar Command in Linux](https://www.geeksforgeeks.org/tar-command-in-linux-with-examples/)

onelinerhub: [How do I unpack a tar file in Unix?](https://onelinerhub.com/cli-tar/how-do-i-unpack-a-tar-file-in-unix)