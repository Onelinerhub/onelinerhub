# How do I use the shell to tar and zip files?
// plain

The shell can be used to tar and zip files using the tar and zip commands.

For example, to tar a directory called `mydir` and store it in a file called `mydir.tar`, the following command can be used:

```
tar -cvf mydir.tar mydir
```

The command will create a tar file called `mydir.tar` in the current working directory.

To zip a directory called `mydir` and store it in a file called `mydir.zip`, the following command can be used:

```
zip -r mydir.zip mydir
```

The command will create a zip file called `mydir.zip` in the current working directory.

## Code explanation


- `tar`: The tar command is used to create tar archives
- `-cvf`: The `-cvf` option is used to create a tar archive with verbose output and store it in a file
- `zip`: The zip command is used to create zip archives
- `-r`: The `-r` option is used to recursively zip a directory

For more information, see the following links:

- [tar command](https://www.computerhope.com/unix/utar.htm)
- [zip command](https://www.computerhope.com/unix/uzip.htm)

onelinerhub: [How do I use the shell to tar and zip files?](https://onelinerhub.com/cli-tar/how-do-i-use-the-shell-to-tar-and-zip-files)