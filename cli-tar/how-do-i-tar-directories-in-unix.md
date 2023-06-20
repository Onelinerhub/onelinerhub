# How do I tar directories in Unix?
// plain

Tarring directories in Unix is a process that allows you to create a single file that contains all the contents of the directories you want to archive. This single file, or tarball, can then be used for backup, distribution, or other purposes.

To tar a directory, use the `tar` command with the `-czvf` flags:

```
tar -czvf <output_filename>.tar.gz <directory_to_tar>
```

This command will create a tarball with the given output filename, containing the contents of the directory specified.

Parts of the command:
- `tar`: the command used to create a tarball
- `-czvf`: the flags used to indicate that the output should be compressed, and that verbose information should be printed
- `<output_filename>.tar.gz`: the name of the tarball that will be created
- `<directory_to_tar>`: the directory to be included in the tarball

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linuxize Tar Tutorial](https://linuxize.com/post/how-to-use-tar-command-in-linux/)

onelinerhub: [How do I tar directories in Unix?](https://onelinerhub.com/cli-tar/how-do-i-tar-directories-in-unix)