# How do I use tar to compress only directories in a Unix system?
// plain

`tar` is a Unix utility used to create and manipulate tar archives. To compress only directories using `tar`, use the `-z` flag for gzip compression and the `-C` flag to specify the directory containing the files to be archived. For example:

```
tar -zcvf archive.tar.gz -C /path/to/directory .
```

This command will create an archive named `archive.tar.gz` containing all the files and directories in `/path/to/directory`.

The parts of the command are as follows:

* `tar`: the command to create and manipulate tar archives
* `-z`: flag to enable gzip compression
* `-c`: flag to create an archive
* `-v`: flag to enable verbose output
* `-f`: flag to specify the output file name
* `-C`: flag to specify the directory containing the files to be archived
* `archive.tar.gz`: the name of the output file
* `/path/to/directory`: the directory containing the files to be archived
* `.`: the current directory

## Helpful links

* [tar man page](https://linux.die.net/man/1/tar)
* [GNU tar documentation](https://www.gnu.org/software/tar/manual/html_node/tar_45.html)

onelinerhub: [How do I use tar to compress only directories in a Unix system?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-to-compress-only-directories-in-a-unix-system)