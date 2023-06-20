# How do I use tar and gzip in Linux?
// plain

Tar and gzip are two of the most popular archiving and compression utilities for Linux.

`tar -cvzf archive.tar.gz <files>`

This command will create an archive file called archive.tar.gz, containing all the files listed in `<files>`.

- `tar`: creates an archive file
- `-c`: creates a new archive
- `-v`: verbose output
- `-z`: compress the archive with gzip
- `-f`: specifies the name of the archive

The archive can be extracted with:

`tar -xvzf archive.tar.gz`

- `-x`: extract files from the archive

Links:

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_21.html)
- [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I use tar and gzip in Linux?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-and-gzip-in-linux)