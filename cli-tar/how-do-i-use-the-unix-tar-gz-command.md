# How do I use the Unix tar gz command?
// plain

The `tar gz` command is used in Unix to create a compressed archive file, also known as a tarball. It combines multiple files into one file and compresses them using the gzip algorithm.

To use the `tar gz` command, you must specify the operation to perform (`c` for create, `x` for extract, `t` for list), the compression format (`z` for gzip compression), and the name of the archive file.

For example, to create a compressed archive of the `/home/user/files` directory, you would run the following command:

```
tar czf archive.tar.gz /home/user/files
```

The command above will create a file named `archive.tar.gz` in the current working directory.

The parts of the command are as follows:

- `tar`: the command to create, extract, or list a tarball
- `c`: the operation to perform (create a tarball)
- `z`: the compression format (gzip)
- `f`: the flag to specify the name of the archive
- `archive.tar.gz`: the name of the archive to create
- `/home/user/files`: the directory to compress

For more information about the `tar gz` command, please see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_13.html).

onelinerhub: [How do I use the Unix tar gz command?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-gz-command)