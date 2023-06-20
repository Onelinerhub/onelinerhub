# How do I tar and gzip a file on a Mac?
// plain

To tar and gzip a file on a Mac, you can use the `tar` command. The syntax for using `tar` to create an archive and compress it in one step is as follows:

```
tar -czvf archive-name.tar.gz /path/to/directory-or-file
```

The flags used are:
- `-c`: create an archive
- `-z`: compress the archive with gzip
- `-v`: show progress in the terminal while creating the archive
- `-f`: allows you to specify the filename of the archive

The output should look something like this:

```
a directory-or-file
a directory-or-file/file1
a directory-or-file/file2
```

Once the command is complete, you will have a `.tar.gz` archive with the specified name in the current working directory.

For more information, see the following links:
- [tar command man page](https://linux.die.net/man/1/tar)
- [How to Create and Extract tar.gz Files in Linux](https://www.howtogeek.com/248780/how-to-create-and-extract-tar-gz-files-in-linux/)

onelinerhub: [How do I tar and gzip a file on a Mac?](https://onelinerhub.com/cli-tar/how-do-i-tar-and-gzip-a-file-on-a-mac)