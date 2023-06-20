# How do I use gzip to tar a file on Linux?
// plain

To use gzip to tar a file on Linux, first you need to install the gzip package if not already installed. This can be done by running the command `sudo apt-get install gzip` or `sudo yum install gzip`.

Once the gzip package is installed, you can use the `tar` command to tar a file. The syntax for this command is `tar -zcvf <filename>.tar.gz <file to be tarred>`. For example, to tar the file `test.txt`, you would use the command `tar -zcvf test.tar.gz test.txt`.

The flags used in the command are:

- `z`: Compress the tar file using gzip
- `c`: Create a new tar archive
- `v`: Verbosely list files which are processed
- `f`: Use archive file or device `<filename>`

After the command is complete, you will have a tarball named `test.tar.gz` which contains the file `test.txt`.

## Helpful links

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [Linux Gzip Tutorial](https://www.guru99.com/gzip-gunzip-linux.html)

onelinerhub: [How do I use gzip to tar a file on Linux?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip-to-tar-a-file-on-linux)