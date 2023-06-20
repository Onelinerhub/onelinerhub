# How do I use shell tiki tar to compress files?
// plain

Shell tiki tar is a command line utility that can be used to compress and archive files. To use it, the `tar` command must be followed by the `-czvf` option and the name of the archive. The `-c` option tells tar to create an archive, the `-z` option tells tar to compress the archive with gzip, the `-v` option tells tar to display progress information, and the `-f` option tells tar to use the following argument as the archive filename.

For example, to compress all the files in the current directory into an archive named `myfiles.tar.gz`, the following command can be used:

```
tar -czvf myfiles.tar.gz *
```

The command above will create a compressed archive named `myfiles.tar.gz` that contains all the files in the current directory.

The following list explains each option used in the command above:

- `-c`: tells tar to create an archive
- `-z`: tells tar to compress the archive with gzip
- `-v`: tells tar to display progress information
- `-f`: tells tar to use the following argument as the archive filename

For more information about using tar, please refer to the following links:

- [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linux tar Command Tutorial with Examples](https://linuxize.com/post/how-to-use-tar-command-in-linux/)

onelinerhub: [How do I use shell tiki tar to compress files?](https://onelinerhub.com/cli-tar/how-do-i-use-shell-tiki-tar-to-compress-files)