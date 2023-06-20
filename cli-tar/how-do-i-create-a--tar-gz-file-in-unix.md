# How do I create a .tar.gz file in Unix?
// plain

Creating a `.tar.gz` file in Unix is a two-step process. First, the files need to be archived into a `.tar` file, and then the `.tar` file needs to be compressed into a `.tar.gz` file.

1. Create a `.tar` file:
   ```
   tar -cvf archive.tar file1 file2 file3
   ```
2. Compress the `.tar` file into a `.tar.gz` file:
   ```
   gzip archive.tar
   ```

This will create a file called `archive.tar.gz` which contains all the files listed.

## Helpful links
* [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html)
* [Gzip Manual](https://www.gnu.org/software/gzip/manual/gzip.html)

onelinerhub: [How do I create a .tar.gz file in Unix?](https://onelinerhub.com/cli-tar/how-do-i-create-a--tar-gz-file-in-unix)