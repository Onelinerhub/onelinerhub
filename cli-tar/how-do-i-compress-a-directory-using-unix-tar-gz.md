# How do I compress a directory using Unix tar gz?
// plain

Compressing a directory using Unix tar gz is a very straightforward process. First, navigate to the directory you wish to compress. Then, run the following command in the terminal:

```
tar -zcvf <target>.tar.gz <source>
```

This command will create a new file called `<target>.tar.gz` in the same directory that contains the compressed version of the `<source>` directory.

Here is a breakdown of the parts of the command:
- `tar`: the Unix command for archiving files
- `-zcvf`: flags for the command, which stand for:
  - `-z`: compress the archive using gzip
  - `-c`: create a new archive
  - `-v`: verbose output
  - `-f`: use an archive file
- `<target>.tar.gz`: the name of the archive file that will be created
- `<source>`: the directory to be compressed

For more information about the `tar` command, refer to the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I compress a directory using Unix tar gz?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-directory-using-unix-tar-gz)