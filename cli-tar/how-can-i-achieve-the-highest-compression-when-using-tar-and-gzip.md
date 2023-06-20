# How can I achieve the highest compression when using tar and gzip?
// plain

The highest compression when using tar and gzip can be achieved by using the **-9** flag. This flag will enable maximum compression, which is the slowest but also the most effective.

## Example code

```
tar -cvzf archive.tar.gz --exclude=*.log * -9
```

This command will create an archive called `archive.tar.gz` and compress all files except for those with the `.log` extension using the maximum compression level.

The parts of the command are as follows:
- `tar`: the command to create the archive
- `-cvzf`: the flags for the command
  - `-c`: create an archive
  - `-v`: verbose output
  - `-z`: compress the archive with gzip
  - `-f`: use archive file
- `archive.tar.gz`: the name of the archive file
- `--exclude=*.log`: exclude all files with the `.log` extension
- `*`: the files and directories to archive
- `-9`: the maximum compression level

For more information about `tar` command, please refer to the following link:

[GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html)

onelinerhub: [How can I achieve the highest compression when using tar and gzip?](https://onelinerhub.com/cli-tar/how-can-i-achieve-the-highest-compression-when-using-tar-and-gzip)