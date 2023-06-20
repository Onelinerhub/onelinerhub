# How do I open a tar.gz file in Unix?
// plain

To open a tar.gz file in Unix, use the `tar` command. This command stands for Tape ARchive, and is used to manipulate files that have been compressed into an archive.

The syntax for the command is as follows:

```
tar -xvzf <file_name>.tar.gz
```

The `-x` flag stands for extract, `-v` for verbose (which will list the files that are extracted), `-z` for gzip (which is the compression algorithm used for this type of file), and `-f` for file.

The output of the command will be a list of the files that have been extracted from the archive:

```
x test.txt
x test2.txt
```

For more information on the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I open a tar.gz file in Unix?](https://onelinerhub.com/cli-tar/how-do-i-open-a-tar-gz-file-in-unix)