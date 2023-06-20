# How do I use tar to compress a directory in a shell?
// plain

The `tar` command can be used to compress a directory in a shell. It is a useful tool for archiving and compressing multiple files and directories into one file.

Here is an example of how to use the `tar` command to compress a directory:

```
tar -czvf myarchive.tar.gz mydirectory/
```

This command will create a `myarchive.tar.gz` file that contains the contents of the `mydirectory` directory. The `-czvf` options used in this command are:

- `-c`: Create a new archive
- `-z`: Compress the archive with gzip
- `-v`: Verbosely list files processed
- `-f`: Specify the filename for the resulting archive

For more information about the `tar` command, see the [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use tar to compress a directory in a shell?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-to-compress-a-directory-in-a-shell)