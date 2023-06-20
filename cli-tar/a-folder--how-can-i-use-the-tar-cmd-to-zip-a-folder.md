# a folder

How can I use the tar cmd to zip a folder?
// plain

The `tar` command can be used to create a compressed archive of a folder. To do this, the `-czvf` flags should be used.

`-c`: Create a new archive
`-z`: Compress the archive using gzip
`-v`: Verbose output
`-f`: Specify an archive filename

For example, to create an archive of a folder called `my_folder`, the following command can be used:

```
tar -czvf my_folder.tar.gz my_folder
```

This command will create a compressed archive of the `my_folder` directory and save it as `my_folder.tar.gz`.

To extract the contents of the archive, the `-x` flag should be used:

```
tar -xzvf my_folder.tar.gz
```

This will extract the contents of the archive into the current directory.

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linux Tutorial - tar Command](https://linuxize.com/post/how-to-use-tar-command-in-linux/)

onelinerhub: [a folder

How can I use the tar cmd to zip a folder?](https://onelinerhub.com/cli-tar/a-folder--how-can-i-use-the-tar-cmd-to-zip-a-folder)