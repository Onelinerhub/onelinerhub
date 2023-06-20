# How do I use Unix tar to compress files into a directory?
// plain

To use Unix tar to compress files into a directory, use the following command:

```
tar -czvf <name_of_archive.tar.gz> <name_of_directory>
```

This will create a compressed archive of the directory in the current working directory.

The parts of the command are as follows:

* `tar`: the command to use for archiving
* `-czvf`: flags to set the compression type (`-c`), verbose output (`-v`), and output file name (`-f`)
* `<name_of_archive.tar.gz>`: the name of the compressed archive to be created
* `<name_of_directory>`: the name of the directory to be compressed

For more information, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/html_node/tar_7.html).

onelinerhub: [How do I use Unix tar to compress files into a directory?](https://onelinerhub.com/cli-tar/how-do-i-use-unix-tar-to-compress-files-into-a-directory)