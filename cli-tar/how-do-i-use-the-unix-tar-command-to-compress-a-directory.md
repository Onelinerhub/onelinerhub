# How do I use the Unix tar command to compress a directory?
// plain

The `tar` command is used to compress and extract files in Unix and Linux systems. To compress a directory, you can use the following command:

```
tar -czvf directory_name.tar.gz directory_name
```

This command will create a compressed `.tar.gz` file in the current working directory.

1. `tar`: This is the command to invoke the tar utility.
2. `-czvf`: This is the set of options used to compress the directory. `-c` creates an archive, `-z` compresses the archive with gzip, `-v` displays the progress of the compression process, and `-f` specifies the filename of the resulting archive.
3. `directory_name.tar.gz`: This is the name of the resulting archive.
4. `directory_name`: This is the name of the directory to be compressed.

For more information on the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the Unix tar command to compress a directory?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-command-to-compress-a-directory)