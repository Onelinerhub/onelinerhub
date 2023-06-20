# How do I use tar to compress a directory in Unix?
// plain

To use tar to compress a directory in Unix, you can use the following command:
```
tar -zcvf <filename>.tar.gz <directory>
```
This will create a tarball file called `<filename>.tar.gz` containing the contents of the directory `<directory>`. The flags `-zcvf` indicate that the tarball should be compressed using gzip, created (`-c`), verbosely listed (`-v`), and the output file should be `<filename>.tar.gz` (`-f`).

## Code explanation

- `tar`: the command to create a tar archive
- `-zcvf`: flags indicating that the tarball should be compressed using gzip, created, verbosely listed, and the output file should be `<filename>.tar.gz`
- `<filename>.tar.gz`: the output file name
- `<directory>`: the directory to be compressed

## Helpful links
- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_7.html)
- [Linuxize - How to Create Tar Gz Archive](https://linuxize.com/post/how-to-create-tar-gz-archive/)

onelinerhub: [How do I use tar to compress a directory in Unix?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-to-compress-a-directory-in-unix)