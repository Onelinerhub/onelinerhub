# How do I extract a tar file using the terminal?
// plain

To extract a tar file using the terminal, you can use the `tar` command with the `-x` option. This command will extract the contents of the tar file into the current directory.

## Example

```
tar -xvf my_file.tar
```

## Output example

```
x file1.txt
x file2.txt
x file3.txt
```

The command consists of the following parts:
- `tar`: the command to extract tar files
- `-x`: the option to extract the tar file
- `-v`: the option to show the progress of the extraction
- `f`: the option to specify the file to extract
- `my_file.tar`: the name of the tar file to be extracted

For more information on the `tar` command, see the following links:
- [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_6.html)
- [Linux man page for tar](http://man7.org/linux/man-pages/man1/tar.1.html)

onelinerhub: [How do I extract a tar file using the terminal?](https://onelinerhub.com/cli-tar/how-do-i-extract-a-tar-file-using-the-terminal)