# How do I use a gzip tar ball?
// plain

A gzip tarball is a file that contains multiple files and folders that have been compressed together into a single file. To use a gzip tarball, you first need to extract it using the `tar` command.

The syntax for extracting a gzip tarball is as follows:

```
tar -xzvf <tarball-name>.tar.gz
```

This command will extract the contents of the tarball into the current directory.

The parts of the command are as follows:

* `-x`: extract files from the tarball
* `-z`: use gzip to decompress the tarball
* `-v`: verbose output (optional)
* `-f`: use the following file as the tarball

For example, if the tarball is called `example.tar.gz`, the command would look like this:

```
tar -xzvf example.tar.gz
```

This command will create a new folder containing the files and folders contained in the tarball.

For more information about using tarballs, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use a gzip tar ball?](https://onelinerhub.com/cli-tar/how-do-i-use-a-gzip-tar-ball)